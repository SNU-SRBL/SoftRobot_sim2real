#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaMatrix" for configuration "MinSizeRel"
set_property(TARGET SofaMatrix APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaMatrix PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaMatrix.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaMatrix.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaMatrix )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaMatrix "${_IMPORT_PREFIX}/lib/SofaMatrix.lib" "${_IMPORT_PREFIX}/bin/SofaMatrix.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
