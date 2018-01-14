#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class RangeV3Vs2015Conan(ConanFile):
    name = "range-v3"
    vcpkg_version = "vcpkg5"
    version = "{}-vs2015".format(vcpkg_version)
    url = "https://github.com/sixten-hilborn/conan-range-v3-vs2015"
    description = "Keep it short"
    
    # Indicates License type of the packaged library
    license = "Boost Software License 1.0"
    
    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    
    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/Microsoft/Range-V3-VS2015"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.vcpkg_version))
        extracted_dir = self.name + "-VS2015-" + self.vcpkg_version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def package(self):
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="LICENSE")
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
