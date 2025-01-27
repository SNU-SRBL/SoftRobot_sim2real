#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaValidation" for configuration "MinSizeRel"
set_property(TARGET SofaValidation APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaValidation PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaValidation.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaValidation.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaValidation )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaValidation "${_IMPORT_PREFIX}/lib/SofaValidation.lib" "${_IMPORT_PREFIX}/bin/SofaValidation.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
