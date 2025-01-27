#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaLoader" for configuration "MinSizeRel"
set_property(TARGET SofaLoader APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaLoader PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaLoader.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaLoader.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaLoader )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaLoader "${_IMPORT_PREFIX}/lib/SofaLoader.lib" "${_IMPORT_PREFIX}/bin/SofaLoader.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
