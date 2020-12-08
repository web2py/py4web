import sys


# Note, when changing the Highlight.js css,
# the background color of .file .diff should match the
# background in the .hljs class in gitlog.min.css
# otherwise there will be a large gap between
# the file name and the

css = """
html {background-color: white; font-family: helvetica}
.file { font-family: courier; white-space: pre; font-size: 18px; margin-bottom: 10px;}
.file .diff { background:#2b2b2b; padding: 10px; marging: 10px;}
.file .filename { background: #f1f1f1; color: #111111; padding: 10px; marging: 10px;}
.line.line-old { color: #ffbbbb; font-weight:bold;}
.line.line-new { color: #bbbbff; font-weight:bold; }
.line:hover {background: #333333; color: yellow;}
.message {padding: 10px; font-size: 20px; }
"""

script = """
hljs.initHighlightingOnLoad();
$('.line:not(.line-new)').each(function(){$(this).text($(this).attr('data-content') + "\\n")});
$('.line-new').hide();
$('.hide-newline').hide();
$('.diff').hide();
$('.file .filename').click(function(){$(this).closest('.file').find('.diff').slideToggle();});
var block = 0;
function draw(){
  if(block>0)
    $('.line-new[data-block="'+block+'"]').each(function(){
      var t = $(this);
      var text = t.attr('data-content');
      var value = t.text();
      var length = value.length;
      if(length<text.length) { t.text(value+text[length]); };
   });
}
setInterval(draw, 50);
$("html").keypress(function(e){
  if(e.key=="n") {
    $('.line-old[data-block="'+block+'"]').hide();
    $('.line-new[data-block="'+block+'"]').show();
    $('.hide-newline[data-block="'+block+'"]').show();
    $('.line-new[data-block="'+block+'"]').each(function(){$(this).text($(this).attr('data-content'));});
    if($('.line[data-block="'+(block+1)+'"]').length==0) return;
    block=block+1;
    $('.line-old[data-block="'+block+'"]').hide();
    $('.line-new[data-block="'+block+'"]').show();
    $('.hide-newline[data-block="'+block+'"]').show();
    $('.line-new[data-block="'+block+'"]').text('');
    $('.line-new[data-block="'+block+'"]').closest('.file').find('.diff').show();
  } else if (e.key=='b') {
    $('.line-old[data-block="'+block+'"]').show();
    $('.line-new[data-block="'+block+'"]').hide();
    $('.hide-newline[data-block="'+block+'"]').hide();
    block=Math.max(0, block-1);
    $('.line-old[data-block="'+block+'"]').hide();
    $('.line-new[data-block="'+block+'"]').show();
    $('.hide-newline[data-block="'+block+'"]').show();
    $('.line-new[data-block="'+block+'"]').text(function(){$(this).text($(this).attr('data-content') );});
    $('.line-new[data-block="'+block+'"]').closest('.file').find('.diff').show();
  } else if (e.key=='v') {
    block=0;
    $('.line-old').show();
    $('.hide-newline').hide();
    $('.line-new').hide().each(function(){$(this).text('');});
  } else if (e.key=='m') {
    block=%i;
    $('.line-old').hide();
    $('.hide-newline').show();
    $('.line-new').show().each(function(){$(this).text($(this).attr('data-content'));});
  }
});
"""


def escape(txt):
    return (
        txt.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


# specify which language we want to render as for highlight.js
# based on the name of the file
def getFileType(name):

    if name.lower().endswith(".py"):
        return 'class="language-python"'
    if name.lower().endswith(".js"):
        return 'class="language-javascript"'
    if name.lower().endswith(".html"):
        return 'class="language-html"'
    if name.lower().endswith(".css"):
        return 'class="language-css"'
    return ""


def diff2kryten(data):
    lines = data.split("\n")
    files = {}
    filename = ""
    message = ""
    mode = 0
    block = 0
    line_old = '<span class="line line-old" data-block="%s" data-content="%s"></span>'
    line_new = '<span class="line line-new" data-block="%s" data-content="%s"></span><span class="hide-newline" data-block="%s">\n</span>'
    line_reg = '<span class="line" data-content="%s"></span>'
    for line in lines:
        if line.startswith("---"):
            filename_a = line[4:].strip()
            if filename_a.startswith("a/"):
                filename_a = filename_a[2:]
            mode = 1
        elif line.startswith("+++"):
            filename_b = line[4:].strip()
            if filename_b.startswith("b/"):
                filename_b = filename_b[2:]
            if filename_a == "/dev/null":
                filename = filename_b
                files[filename] = {"mode": "create", "lines": []}
            elif filename_b == "/dev/null":
                filename = filename_a
                files[filename] = {"mode": "delete", "lines": []}
            else:
                filename = filename_a
                files[filename] = {"mode": "edit", "lines": []}
            mode = 2
        elif line.startswith("-"):
            mode, block = 3, block + 1
            files[filename]["lines"].append(line_old % (block, escape(line[1:])))
        elif line.startswith("+"):
            mode, block = 3, block + 1
            files[filename]["lines"].append(line_new % (block, escape(line[1:]), block))
        elif line.startswith(" ") and mode >= 2:
            files[filename]["lines"].append(line_reg % escape(line[1:]))
            if mode > 2:
                mode = 2
        elif line.startswith(" ") and mode < 2:
            message += escape(line.strip()) + "<br/>"
        else:
            pass
    div = '<div class="message">%s</div>' % message
    for filename in sorted(files):
        mode = files[filename]["mode"]
        if mode != "delete":
            lines = "".join(files[filename]["lines"])
        div += '<div class="file">'
        div += '<div class="filename">%s (%s)</div>' % (filename, mode)
        div += '<div class="diff"><pre><code %s>%s</code></pre></div></div>' % (
            getFileType(filename),
            lines,
        )
    return (
        "<html><head>"
        + """<link rel="stylesheet"
          href="/_dashboard/static/css/gitlog.min.css">"""
        + "<style>"
        + css
        + '</style></head><body><div style="text-align:right">'
        + "</div>"
        + div
        + '<script src="/_dashboard/static/js/jquery.min.js"></script>'
        + '<script src="/_dashboard/static/js/highlight.min.js"></script>'
        + "<script>"
        + (script % block)
        + "</script></body></html>"
    )


if __name__ == "__main__":
    print(diff2kryten(open(sys.argv[1], "r").read()))
