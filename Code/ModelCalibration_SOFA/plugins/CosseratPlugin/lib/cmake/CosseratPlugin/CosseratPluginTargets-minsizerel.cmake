#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "CosseratPlugin" for configuration "MinSizeRel"
set_property(TARGET CosseratPlugin APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(CosseratPlugin PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/CosseratPlugin.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/CosseratPlugin.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS CosseratPlugin )
list(APPEND _IMPORT_CHECK_FILES_FOR_CosseratPlugin "${_IMPORT_PREFIX}/lib/CosseratPlugin.lib" "${_IMPORT_PREFIX}/bin/CosseratPlugin.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
