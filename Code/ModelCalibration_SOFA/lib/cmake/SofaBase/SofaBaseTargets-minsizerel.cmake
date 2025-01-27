#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaBase" for configuration "MinSizeRel"
set_property(TARGET SofaBase APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaBase PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaBase.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaBase.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaBase )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaBase "${_IMPORT_PREFIX}/lib/SofaBase.lib" "${_IMPORT_PREFIX}/bin/SofaBase.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
