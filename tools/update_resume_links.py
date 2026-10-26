from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = {
    './Lyoneh%20Gbojueh%20Resume.pdf': './Resume.pdf',
    'Lyoneh%20Gbojueh%20Resume.pdf': 'Resume.pdf',
    './Lyoneh Gbojueh Resume.pdf': './Resume.pdf',
    'Lyoneh Gbojueh Resume.pdf': 'Resume.pdf',
    'download="Lyoneh_Gbojueh_Resume.pdf"': 'download="Resume.pdf"',
}

for old, new in replacements.items():
    text = text.replace(old, new)

path.write_text(text, encoding='utf-8')
print('Updated portfolio resume references to Resume.pdf')
