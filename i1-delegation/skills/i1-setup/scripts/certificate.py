#!/usr/bin/env python3
"""Make the i1 delegation setup certificate.

Usage:  python3 certificate.py "Coach Full Name" "October 9, 2026" out.pdf [fr]
Needs:  reportlab (pip install reportlab). Fonts are in ./fonts next to this file.
Output: a one-page landscape PDF. Same look every time; only the name and date change.
"""
import os, sys
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

STR = {
    'en': dict(prog='STUDENT WORKS  ·  MANAGEMENT PROGRAM', title='Certificate of Setup', sub='i1 DELEGATION',
               cert='This certifies that', l1='has set up i1 delegation and handed the busywork to Claude.',
               l2='Texts, sheet, i2 bookings, Recruitee and call reminders now run on their own.', date='DATE', sig='i1 DELEGATION'),
    'fr': dict(prog='STUDENT WORKS  ·  PROGRAMME DE GESTION', title='Certificat de configuration', sub='DÉLÉGATION i1',
               cert='Ceci certifie que', l1='a configuré la délégation i1 et confié les tâches répétitives à Claude.',
               l2='Textos, feuille, réservations i2, Recruitee et rappels d\'appel se font maintenant tout seuls.', date='DATE', sig='DÉLÉGATION i1'),
}

def main(name, date, out, lang='en'):
    T = STR.get(lang, STR['en'])
    here = os.path.dirname(os.path.abspath(__file__))
    fd = os.path.join(here, 'fonts')
    for n, f in [('Playfair', 'PlayfairDisplay-Bold.ttf'), ('Mont', 'Montserrat-Regular.ttf'),
                 ('MontSB', 'Montserrat-SemiBold.ttf'), ('Pinyon', 'Pinyon.ttf'), ('Vibes', 'GreatVibes-Regular.ttf')]:
        pdfmetrics.registerFont(TTFont(n, os.path.join(fd, f)))
    W, H = landscape(letter)
    red = HexColor('#a50f24'); red2 = HexColor('#7a0b1a'); dark = HexColor('#1c1c1c'); grey = HexColor('#6b6b6b')
    cream = HexColor('#fdf8ef'); gold = HexColor('#c9a227'); gold2 = HexColor('#e6c76a')
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle('i1 delegation certificate')
    c.setFillColor(cream); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(red); c.rect(0, H - 34, W, 34, fill=1, stroke=0); c.rect(0, 0, W, 34, fill=1, stroke=0)
    c.setFillColor(gold); c.rect(0, H - 38, W, 4, fill=1, stroke=0); c.rect(0, 34, W, 4, fill=1, stroke=0)
    c.setStrokeColor(gold); c.setLineWidth(3); c.rect(48, 52, W - 96, H - 104, fill=0)
    c.setStrokeColor(red); c.setLineWidth(1); c.rect(56, 60, W - 112, H - 120, fill=0)
    def corner(x, y, sx, sy):
        c.setStrokeColor(gold); c.setLineWidth(2); c.line(x, y + sy * 34, x + sx * 34, y)
        c.setLineWidth(1); c.line(x + sx * 8, y + sy * 44, x + sx * 44, y + sy * 8)
        c.setFillColor(red); c.circle(x + sx * 20, y + sy * 20, 3, fill=1, stroke=0)
    for a in [(56, 60, 1, 1), (W - 56, 60, -1, 1), (56, H - 60, 1, -1), (W - 56, H - 60, -1, -1)]: corner(*a)
    c.setFillColor(red); c.setFont('MontSB', 10.5); c.drawCentredString(W / 2, H - 96, ' '.join(T['prog']))
    c.setFillColor(dark); c.setFont('Playfair', 46); c.setFont('Playfair', 46 if lang == 'en' else 40); c.drawCentredString(W / 2, H - 152, T['title'])
    c.setStrokeColor(gold); c.setLineWidth(1.2); c.line(W / 2 - 110, H - 170, W / 2 - 10, H - 170); c.line(W / 2 + 10, H - 170, W / 2 + 110, H - 170)
    c.setFillColor(gold); p = c.beginPath(); p.moveTo(W / 2, H - 164); p.lineTo(W / 2 + 6, H - 170); p.lineTo(W / 2, H - 176); p.lineTo(W / 2 - 6, H - 170); p.close(); c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(red); c.setFont('MontSB', 12); c.drawCentredString(W / 2, H - 196, ' '.join(T['sub']))
    c.setFillColor(grey); c.setFont('Mont', 12.5); c.drawCentredString(W / 2, H - 240, T['cert'])
    # name: shrink long names so they always fit
    size = 64
    while pdfmetrics.stringWidth(name, 'Pinyon', size) > W - 200 and size > 30: size -= 2
    ny = H - 306
    c.setFont('Pinyon', size)
    c.setFillColor(gold2); c.drawCentredString(W / 2 + 1.6, ny - 1.6, name)
    c.setFillColor(red2); c.drawCentredString(W / 2, ny, name)
    c.setStrokeColor(gold); c.setLineWidth(1.2); c.line(W / 2 - 230, ny - 18, W / 2 + 230, ny - 18)
    c.setFillColor(gold); c.circle(W / 2 - 230, ny - 18, 2.5, fill=1, stroke=0); c.circle(W / 2 + 230, ny - 18, 2.5, fill=1, stroke=0)
    c.setFillColor(dark); c.setFont('Mont', 13)
    c.drawCentredString(W / 2, H - 354, T['l1'])
    c.drawCentredString(W / 2, H - 374, T['l2'])
    cx, cy = W / 2, 122
    c.setFillColor(gold); c.circle(cx, cy, 36, fill=1, stroke=0)
    c.setFillColor(cream); c.circle(cx, cy, 32, fill=1, stroke=0)
    c.setFillColor(red); c.circle(cx, cy, 28, fill=1, stroke=0)
    c.setStrokeColor(gold2); c.setLineWidth(0.8); c.circle(cx, cy, 23, fill=0)
    c.setFillColor(cream); c.setFont('Playfair', 17); c.drawCentredString(cx, cy - 6, 'i1')
    c.setFillColor(red)
    for sx in (-1, 1):
        p = c.beginPath(); p.moveTo(cx + sx * 10, cy - 26); p.lineTo(cx + sx * 22, cy - 56); p.lineTo(cx + sx * 12, cy - 50); p.lineTo(cx + sx * 2, cy - 58); p.close(); c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(dark); c.setFont('Mont', 10.5); c.drawString(96, 118, date)
    c.setFillColor(grey); c.setFont('MontSB', 8); c.drawString(96, 104, T['date'])
    c.setFillColor(red2); c.setFont('Vibes', 24); c.drawRightString(W - 96, 122, 'Student Works')
    c.setFillColor(grey); c.setFont('MontSB', 8); c.drawRightString(W - 96, 104, T['sig'])
    # maker's mark: tiny initials in the bottom band, same colour family as the band
    c.setFillColor(HexColor('#b8203a')); c.setFont('MontSB', 6); c.drawRightString(W - 30, 12, 'ZH')
    c.setAuthor('ZH')
    c.save()

if __name__ == '__main__':
    if len(sys.argv) not in (4, 5):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) == 5 else 'en')
