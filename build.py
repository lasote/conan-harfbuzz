from conan.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="harfbuzz:shared", pure_c=True) 
    builder.run()