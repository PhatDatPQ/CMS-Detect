HTTP_PREFIXS: tuple = (
    'http',
    'https'
)

ENDPOINTS: tuple = (
    '',
    'administrator/help/en-GB/toc.json',
    '/administrator/language/en-GB/install.xml',
    '/plugins/system/debug/debug.xml',
    '/administrator/',
    '/wp-includes/js/jquery/jquery.js',
    '/misc/ajax.js',
    '/admin/view/javascript/common.js',
    '/admin/includes/general.js',
    '/images/editor/separator.gif',
    '/js/header-rollup-554.js'
)

DETECTION: dict = {
    'Wordpress' : [
        '/wp-content/',
        '/wp-inclues/', 
        '(c) jQuery Foundation'
    ],
    
    'Joomla' : [
        '"COMPONENTS_BANNERS_BANNERS"', 
        '<author>Joomla!', 
        'content="Joomla!'
    ],
    
    'drupal' : [
        'Drupal.ajax', 
        '/sites/default/files'
    ],
    
    'Opencart' : [
        'getURLVar(key)'
    ],
    
    'osCommerce' : [
        'function SetFocus()'
    ],
    
    'vBulletin' : [
        'GIF89a', 
        'js.compressed/modernizr.min.js', 
        'content="vBulletin'
    ],
    
    'prestashop' : [
        'var prestashop ='
    ]
}
