#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaFramework" for configuration "MinSizeRel"
set_property(TARGET SofaFramework APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaFramework PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaFramework.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaFramework.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaFramework )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaFramework "${_IMPORT_PREFIX}/lib/SofaFramework.lib" "${_IMPORT_PREFIX}/bin/SofaFramework.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
