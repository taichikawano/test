def get(event, context):
    
    html = '''
<head>
</head>
<body>
<h1>Test</h1>
</body>
</html>
'''[1:-1]
    
    return {
        'type': 'html',
        'html': html
    };