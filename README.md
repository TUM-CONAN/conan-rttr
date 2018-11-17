# conan-rttr


[Conan.io](https://conan.io) package for [rttr](https://www.rttr.org) project.

The packages generated with this *conanfile.py* .

## Basic setup

    $ conan install rttr/0.9.7-dev@camposs/testing

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    rttr/0.9.7-dev@camposs/testing

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)
