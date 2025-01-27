#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaOpenglVisual" for configuration "MinSizeRel"
set_property(TARGET SofaOpenglVisual APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaOpenglVisual PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaOpenglVisual.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaOpenglVisual.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaOpenglVisual )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaOpenglVisual "${_IMPORT_PREFIX}/lib/SofaOpenglVisual.lib" "${_IMPORT_PREFIX}/bin/SofaOpenglVisual.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
