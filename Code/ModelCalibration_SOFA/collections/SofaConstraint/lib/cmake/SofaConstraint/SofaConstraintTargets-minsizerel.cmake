#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaConstraint" for configuration "MinSizeRel"
set_property(TARGET SofaConstraint APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaConstraint PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaConstraint.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaConstraint.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaConstraint )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaConstraint "${_IMPORT_PREFIX}/lib/SofaConstraint.lib" "${_IMPORT_PREFIX}/bin/SofaConstraint.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
