def get(event, context):
    
    html = '''
<head>
<style>
h1 {
    color: red;
}
</style>
</head>
<body>
<h1>Test</h1>
<p>Version 5</p>
</body>
</html>
'''[1:-1]
    
    return {
        'type': 'html',
        'html': html
    };
