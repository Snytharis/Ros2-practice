from setuptools import find_packages, setup

package_name = 'mini_haberlesme'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='Mini haberlesme paketi',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'number_publisher = mini_haberlesme.number_publisher:main',
            'number_doubler = mini_haberlesme.number_doubler:main',
        ],
    },
)