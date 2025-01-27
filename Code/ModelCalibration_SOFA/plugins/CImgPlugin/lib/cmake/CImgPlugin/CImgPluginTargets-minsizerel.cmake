#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "CImgPlugin" for configuration "MinSizeRel"
set_property(TARGET CImgPlugin APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(CImgPlugin PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/CImgPlugin.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/CImgPlugin.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS CImgPlugin )
list(APPEND _IMPORT_CHECK_FILES_FOR_CImgPlugin "${_IMPORT_PREFIX}/lib/CImgPlugin.lib" "${_IMPORT_PREFIX}/bin/CImgPlugin.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
