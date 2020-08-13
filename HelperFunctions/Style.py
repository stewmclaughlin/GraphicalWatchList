def tabs_styles():
    return {
        'height': '44px'
    }


def tab_style():
    return {
        'borderBottom': '2px solid #d6d6d6',
        'padding': '6px',
        'fontWeight': 'bold',
        'fontSize': '20px',
        'backgroundColor': '#a262a9'
    }


def tab_selected_style():
    return {
        'borderTop': '2px solid #d6d6d6',
        'borderBottom': '2px solid #d6d6d6',
        'backgroundColor': '#119DFF',
        'color': 'white', 'fontWeight': 'bold', 'fontSize': '20px',
        'padding': '6px'
    }


def checklist_style():
    return {'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'}


def fixed(top, right, width):
    return {"position": "fixed", "top": int(top), "right": int(right), "width": int(width)}


def inline(width):
    return {'width': str(width) + "%", 'display': 'inline-block', 'vertical-align': 'top'}


def inlineWithLeftPadding(width, padding):
    return {'width': str(width) + "%", 'display': 'inline-block', 'vertical-align': 'top',
            'padding-left': str(padding) + "%"}
