import sys

css = """
* { border: 0; margni:0; padding: 0;}
html {background-color: white;}
.file { font-family: courier; white-space: pre; font-size: 18px; margin-bottom: 10px;}
.file .diff {background: #111111; color: #f1f1f1; padding: 10px; marging: 10px;}
.file .filename { background: #f1f1f1; color: #111111; padding: 10px; marging: 10px;} 
.line.line-old { color: #ffbbbb }
.line.line-new { color: #bbbbff }
.line:hover {background: #333333; color: yellow;}
.message {padding: 10px; font-size: 20px; }
"""

script = """
$('.line:not(.line-new)').each(function(){$(this).text($(this).attr('data-content'));});
$('.line-new').hide();
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
  if(e.key=="m") {
  $('.line-old[data-block="'+block+'"]').hide();                                                                                      
  $('.line-new[data-block="'+block+'"]').show();  
  $('.line-new[data-block="'+block+'"]').each(function(){$(this).text($(this).attr('data-content'));});
  block=Math.min(100, block+1); 
  $('.line-old[data-block="'+block+'"]').hide();                                                                                      
  $('.line-new[data-block="'+block+'"]').show();
  $('.line-new[data-block="'+block+'"]').text('');
  $('.line-new[data-block="'+block+'"]').closest('.file').find('.diff').show();
} else if (e.key=='n') {
  $('.line-old[data-block="'+block+'"]').show();                                                                                          
  $('.line-new[data-block="'+block+'"]').hide();
  block=Math.max(0, block-1);
  $('.line-old[data-block="'+block+'"]').hide();                                                                                      
  $('.line-new[data-block="'+block+'"]').show();
  $('.line-new[data-block="'+block+'"]').text(function(){$(this).text($(this).attr('data-content'));});
  $('.line-new[data-block="'+block+'"]').closest('.file').find('.diff').show();
}});
"""

def escape(txt):
    return txt.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

def diff2kryten(data):
    lines = data.split('\n')
    files = {}
    filename = ''
    message = ''
    mode = 0
    block = 0
    for line in lines:
        if line.startswith('---'):
            filename_a = line[4:].strip()
            if filename_a.startswith('a/'): filename_a = filename_a[2:]
            mode = 1
        elif line.startswith('+++'):
            filename_b = line[4:].strip()
            if filename_b.startswith('b/'): filename_b = filename_b[2:]
            if filename_a == '/dev/null':
                filename = filename_b
                files[filename]={'mode': 'create', 'lines':[]}
            elif filename_b == '/dev/null':
                filename = filename_a
                files[filename]={'mode': 'delete', 'lines':[]}
            else:
                filename = filename_a
                files[filename]={'mode': 'edit', 'lines':[]}
            mode = 2
        elif line.startswith('-'):
            mode, block = 3, block + 1
            files[filename]['lines'].append('<div class="line line-old" data-block="%s" data-content="%s"></div>' % (block, escape(line[1:])))
        elif line.startswith('+'):
            mode, block = 3, block + 1
            files[filename]['lines'].append('<div class="line line-new" data-block="%s" data-content="%s"></div>' % (block, escape(line[1:])))
        elif line.startswith(' ') and mode >= 2:
            files[filename]['lines'].append('<div class="line" data-content="%s"></div>' % escape(line[1:]))
            if mode>2: mode = 2
        elif line.startswith(' ') and mode < 2:
            message += escape(line.strip()) + '<br/>'
        else:
            pass
    div = '<div class="message">%s</div>' % message
    for filename in sorted(files):
        mode = files[filename]['mode']
        lines = ''.join(files[filename]['lines'])
        div+='<div class="file"><div class="filename">%s (%s)</div><div class="diff">%s</div></div>' % (filename, mode, lines)
    return '<html><head><style>'+css+'</style></head><body>'+div+'<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script><script>'+script+'</script></body></html>'

if __name__ == '__main__':
    print(diff2kryten(open(sys.argv[1], 'r').read()))
