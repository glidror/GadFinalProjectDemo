

def htmlspecialchars(text):
    return (
        text.replace("&", "&amp;").
        replace('"', "&quot;").
        replace("<", "&lt;").
        replace(">", "&gt;")
    )
