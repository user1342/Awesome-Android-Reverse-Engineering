#! /usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import codecs
import urllib.request, json 





API_URL =  os.environ['INPUT_STORE']
 	

with urllib.request.urlopen(f"{API_URL}") as url:
    data = json.loads(url.read().decode())
    SiteDescription = data['description']
    SiteTitle = data['name']
    Author = data['owner']['login']
   



# README File Path
input_file = "README.md"
input_file_contents = None

# Open our README file 
try:
    with open(input_file, 'r') as f:
        input_file_contents = f.read()
        
except IOError:
    sys.exit('README.md file does not exist, or has no content.  Exiting')


output_file = "index.html"

# Write out the Index.HTML file 
try:
    with codecs.open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"""<head><title>{SiteTitle}</title>
	
	<!-- Primary Meta Tags -->
            <meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="title" content="{SiteTitle}">
<meta name="description" content="{SiteDescription}">
<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://{Author}.github.io/{SiteTitle}">
<meta property="og:title" content="{SiteDescription}">
<meta property="og:description" content="{SiteDescription}">
<meta property="og:image" content="https://og-image.vercel.app/{SiteTitle}.png?theme=light&md=0&fontSize=100px&images=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Ffront%2Fassets%2Fdesign%2Fhyper-color-logo.svg">
<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="https://{Author}.github.io/{SiteTitle}">
<meta property="twitter:title" content="{SiteTitle}">
<meta property="twitter:description" content="{SiteDescription}">
<meta property="twitter:image" content="https://og-image.vercel.app/{SiteTitle}.png?theme=light&md=0&fontSize=100px&images=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Ffront%2Fassets%2Fdesign%2Fhyper-color-logo.svg">
	   
	 
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.28.0/prism.min.js"></script>   
     </head>""" + """
<!--Body Content -->
<body>
<github-md>
""" + 

   input_file_contents + """
    </github-md>
	</body>
	 <script src="https://cdn.jsdelivr.net/gh/MarketingPipeline/Markdown-Tag/markdown-tag-GitHub.js"></script> 
	""")
except IOError:
    sys.exit(u'Unable to write to file: {0}'.format(output_file))
