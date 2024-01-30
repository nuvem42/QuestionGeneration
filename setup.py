from setuptools import setup
setup(
    # ...
    name='example_project',

    # Require this package, but only for setup (not installation):
    setup_requires=['protobuf_distutils'],

    options={
        # See below for details.
        'generate_py_protobufs': {
            'source_dir':        'path/to/protos',
            'extra_proto_paths': ['path/to/other/project/protos'],
            'output_dir':        'path/to/project/sources',  # default '.'
            'proto_files':       ['relative/path/to/just_this_file.proto'],
            'protoc':            'path/to/protoc.exe',
        },
    },
)