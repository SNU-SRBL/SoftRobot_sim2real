#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaCUDA" for configuration "MinSizeRel"
set_property(TARGET SofaCUDA APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaCUDA PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaCUDA.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaCUDA.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaCUDA )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaCUDA "${_IMPORT_PREFIX}/lib/SofaCUDA.lib" "${_IMPORT_PREFIX}/bin/SofaCUDA.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
