with open('main.py', 'r') as src:
    script = src.read()
with open('artifact.html', 'w') as output:
    with open('index.html', 'r') as template:
        tpl = template.read()
        out_text = tpl.format(script=script)
        output.write(out_text)