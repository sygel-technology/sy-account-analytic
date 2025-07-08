import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-account-analytic",
    description="Meta package for sygel-technology-sy-account-analytic Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_analytic_distribution_with_account>=16.0dev,<16.1dev',
        'odoo-addon-account_timesheet_time_type>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
