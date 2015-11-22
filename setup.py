from distutils.core import setup

if __name__ == "__main__":
    setup(name='ascii_art',
          version='0.2.0',
          description='Image to ASCII art generator',
          author='Jonathan Reed',
          author_email='jontonsoup4@gmail.com',
          url='https://github.com/jontonsoup4/ascii_art',
          install_requires=['Pillow>=3.0.0'],
          packages=['ascii_art'],
          package_dir={'ascii_art': 'ascii_art'},
          )
