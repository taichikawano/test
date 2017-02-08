def get(event, context):
    
    html = '''
<head>
<style>
.test-div {
    background: rgba(255,255,255,0.5)
}

h1 {
    color: red;
}
</style>
</head>
<body>
<div class="test-div">
    <h1>Test</h1>
    <p>Version 5</p>
</div>
</body>
</html>
'''[1:-1]
    
    return {
        'type': 'html',
        'html': html
    };
