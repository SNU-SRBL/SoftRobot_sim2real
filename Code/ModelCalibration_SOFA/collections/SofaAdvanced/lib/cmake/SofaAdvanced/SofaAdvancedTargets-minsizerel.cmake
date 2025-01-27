#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaAdvanced" for configuration "MinSizeRel"
set_property(TARGET SofaAdvanced APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaAdvanced PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaAdvanced.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaAdvanced.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaAdvanced )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaAdvanced "${_IMPORT_PREFIX}/lib/SofaAdvanced.lib" "${_IMPORT_PREFIX}/bin/SofaAdvanced.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
