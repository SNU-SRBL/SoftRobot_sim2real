#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaGeneralTopology" for configuration "MinSizeRel"
set_property(TARGET SofaGeneralTopology APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaGeneralTopology PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaGeneralTopology.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaGeneralTopology.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaGeneralTopology )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaGeneralTopology "${_IMPORT_PREFIX}/lib/SofaGeneralTopology.lib" "${_IMPORT_PREFIX}/bin/SofaGeneralTopology.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
