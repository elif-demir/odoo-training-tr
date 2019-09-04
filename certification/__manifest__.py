{
    'name': 'Certification',
    'summary': "Defines certification for different purposes.",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/elif-demir",
    'category': 'Certification Management',
    'verison': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': ['security/certification_security.xml',
             'security/ir.model.access.csv',
             'views/certification_view.xml',
             'views/res_partner_view.xml',
             'views/standard_view.xml'
             ],
    'demo': ['data/certification_data.xml'],
    'development_status': 'Beta',
    'maintainers': ['certificent'],
}
