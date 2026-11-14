"""Rebuild current assessment PDFs from the synchronized knowledgebase digests.

Run unspace_glenn_claim_checks.py first. Requires numpy, matplotlib, reportlab,
pypdf and Windows DejaVu fonts. Overwrites the existing PDFs without backups.
Markdown HTML page/figure comments control layout. Source papers are untouched.
"""
from pathlib import Path
import ast
import io
import json
import re
import subprocess
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak, Image
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
R = json.loads((HERE/'results.json').read_text(encoding='utf-8'))
C = json.loads(subprocess.check_output([sys.executable, str(HERE/'independent_review_checks_2026-11-13.py')], text=True))
tree = ast.parse((HERE/'unspace_glenn_claim_checks.py').read_text(encoding='utf-8'))
T3 = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id=='table3' for t in n.targets))
for name, file in [('DV','DejaVuSans.ttf'),('DV-B','DejaVuSans-Bold.ttf'),('DV-I','DejaVuSans-Oblique.ttf'),('DV-BI','DejaVuSans-BoldOblique.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DV-B', italic='DV-I', boldItalic='DV-BI')
INK, MUTED, RULE, PALE = [colors.HexColor(x) for x in ['#17232f','#52616c','#cbd5dc','#edf3f8']]
W = 6.9*inch
B = ParagraphStyle('body', fontName='DV', fontSize=9.6, leading=13.1, textColor=INK, spaceAfter=6)
S = ParagraphStyle('small', parent=B, fontSize=8.1, leading=10.6, spaceAfter=4)
H = ParagraphStyle('h', parent=B, fontName='DV-B', fontSize=12.5, leading=16.5, spaceAfter=9, keepWithNext=True)
H2 = ParagraphStyle('h2', parent=B, fontName='DV-B', fontSize=10.3, leading=14, spaceBefore=6, spaceAfter=4, keepWithNext=True)
TITLE = ParagraphStyle('title', parent=B, fontName='DV-B', fontSize=17, leading=21, spaceAfter=9)
CELL = ParagraphStyle('cell', parent=B, fontSize=8.5, leading=11.2, spaceAfter=0)

def inline(s):
    s=s.replace('\u2013','-').replace('\u2014',' - ').replace('\u2011','-')
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<link href="\2" color="#2769a5">\1</link>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'\1',s)
    return s

def p(s,style=B):
    return Paragraph(inline(s),style)

def figure(kind):
    if kind=='unspace':
        fig,ax=plt.subplots(figsize=(6.7,2.8))
        ws=np.geomspace(95,6000,200)
        ax.set_xscale('log'); ax.set_yscale('log')
        ax.scatter([r[0] for r in T3],np.abs([r[5] for r in T3]),s=21,color='#2769a5',zorder=4,label='Measured rotation deflection (Table 3)')
        ax.axhline(C['mean_static_rad'],color='#52616c',linestyle='--',label='Mean static deflection')
        ax.plot(ws,R['unspace_newtonian_deformation_dtheta_rad']*(ws/5462.76)**2,color='#219d77',label='Rough deformation scale (disk approximation)')
        ax.plot(ws,R['unspace_GR_expected_dtheta_rad']*(ws/5462.76)**2,color='#d16b39',label='GR rotational-energy scale (not full source model)')
        ax.set(xlim=(90,6500),ylim=(1e-18,.15),xlabel='Rotor angular velocity (rad/s)',ylabel='Angular deflection (rad)')
        ax.legend(loc='center left',fontsize=7.1,framealpha=.94)
    else:
        fig,ax=plt.subplots(figsize=(6.7,2.2))
        vals=[R['glenn_wavelength_ratio_650_532'],R['glenn_refractive_nm_ratio_532_650'],1.,1.]
        yp=np.arange(4)[::-1]
        ax.barh(yp,vals,height=.48,color=['#b36d46','#2769a5','#7b929f','#52616c'])
        ax.set_yticks(yp,['Claimed refractive ratio','Air-density OPL change','Same geometric OPL change','Reported peak ratio'],fontsize=8)
        for y,v,t in zip(yp,vals,['1.222','1.0068','1.000','about 1; uncertainty absent']):
            ax.text(v+.016,y,t,va='center',fontsize=7.5)
        ax.axvline(1,color='#8b969f',linestyle=':',linewidth=1)
        ax.set(xlim=(0,1.65),xlabel='Ratio of OPL changes in nm: 532 nm / 650 nm')
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(labelsize=8,colors='#52616c')
    ax.set_axisbelow(True)
    ax.grid(True,axis='x' if kind=='glenn' else 'both',color='#e2e7eb',linewidth=.65)
    ax.xaxis.label.set_size(8.5); ax.yaxis.label.set_size(8.5)
    fig.tight_layout()
    buf=io.BytesIO()
    fig.savefig(buf,format='png',dpi=220,bbox_inches='tight',facecolor='white')
    plt.close(fig); buf.seek(0)
    im=Image(buf); im.drawWidth=6.7*inch; im.drawHeight=im.drawWidth*im.imageHeight/im.imageWidth
    return im

def build(kind,stem,digest,expected):
    src=ROOT/'00_Knowledgebase'/'sources'/digest
    text=src.read_text(encoding='utf-8')
    story=[]; title=''; headings=[]; refmode=False
    for block in re.split(r'\n\s*\n',text.strip()):
        if block.startswith('<!-- page -->'):
            story.append(PageBreak()); refmode=False; continue
        if block.startswith('<!-- figure:'):
            story.append(figure(kind)); continue
        if block.startswith('# '):
            title=block[2:]; headings.append(title)
            story.extend([p('ANTIGRAVITY PROJECT / REVISED TECHNICAL ASSESSMENT',S),p(title,TITLE),p('13 November 2026 | Original analysis: Claude Opus 5.5',S),p('Revised and checked with GPT-6 Astra Extra High',S),Spacer(1,7)])
        elif block.startswith('## '):
            story.append(p(block[3:],H)); headings.append(block[3:])
        elif block.startswith('### '):
            story.append(p(block[4:],H2)); refmode=block[4:].startswith('Sources and reproducible')
        elif block.startswith('|'):
            rows=[]
            for line in block.splitlines():
                row=[s.strip() for s in line.strip().strip('|').split('|')]
                if all(re.fullmatch(r'[-: ]+',s) for s in row): continue
                rows.append(row)
            fractions=([.35,.65] if len(rows[0])==2 else [.40,.23,.37])
            cells=[[p(('<b>'+s+'</b>') if i==0 else s,CELL) for s in row] for i,row in enumerate(rows)]
            t=Table(cells,colWidths=[W*f for f in fractions],repeatRows=1)
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('GRID',(0,0),(-1,-1),.4,RULE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            story.extend([t,Spacer(1,8)])
        elif block.startswith('> '):
            t=Table([[p(block[2:])]],colWidths=[W])
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('LINEBEFORE',(0,0),(0,-1),3,colors.HexColor('#2769a5')),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
            story.extend([t,Spacer(1,9)])
        elif block.startswith('- '):
            style=ParagraphStyle('bullet',parent=B,leftIndent=10,firstLineIndent=-10)
            story.extend(p('•  '+line[2:],style) for line in block.splitlines())
        else:
            story.append(p(block,S if refmode or block.startswith('**Figure ') else B))
    out=ROOT/'01_Reports-and-Syntheses'/stem
    def footer(c,doc):
        c.saveState(); c.setFont('DV',7.4); c.setFillColor(MUTED)
        c.drawString(.8*inch,.36*inch,f'{kind.title()} assessment | Revised 13 Nov 2026')
        c.drawRightString(letter[0]-.8*inch,.36*inch,f'{doc.page} / {expected}')
        c.setStrokeColor(RULE); c.line(.8*inch,.55*inch,letter[0]-.8*inch,.55*inch); c.restoreState()
    doc=SimpleDocTemplate(str(out),pagesize=letter,leftMargin=.8*inch,rightMargin=.8*inch,topMargin=.65*inch,bottomMargin=.75*inch,title=title,author='Antigravity project - Revised and checked with GPT-6 Astra Extra High',subject='Revised technical assessment, 13 November 2026',creator=Path(__file__).name)
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    reader=PdfReader(out)
    if len(reader.pages)!=expected:
        raise RuntimeError(f'{out.name}: expected {expected} pages, got {len(reader.pages)}')
    for page,heading in zip(reader.pages,headings):
        if ' '.join(heading.split()) not in ' '.join(page.extract_text().split()):
            raise RuntimeError(f'Missing page heading {heading}')
    print(f'{out} | {len(reader.pages)} pages | {out.stat().st_size:,} bytes')

if __name__=='__main__':
    build('unspace','Unspace-Radial-Stress-Torsion-Balance-Technical-Assessment-2026-11-13.pdf','lentz2026-unspace-radial-stress-torsion-balance.md',6)
    build('glenn','Glenn-Spark-Gap-Interferometry-Technical-Assessment-2026-11-13.pdf','glenn2025-spark-gap-interferometry.md',5)
