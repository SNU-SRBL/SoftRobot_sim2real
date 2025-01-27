#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ArticulatedSystemPlugin" for configuration "MinSizeRel"
set_property(TARGET ArticulatedSystemPlugin APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(ArticulatedSystemPlugin PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/ArticulatedSystemPlugin.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/ArticulatedSystemPlugin.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS ArticulatedSystemPlugin )
list(APPEND _IMPORT_CHECK_FILES_FOR_ArticulatedSystemPlugin "${_IMPORT_PREFIX}/lib/ArticulatedSystemPlugin.lib" "${_IMPORT_PREFIX}/bin/ArticulatedSystemPlugin.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
