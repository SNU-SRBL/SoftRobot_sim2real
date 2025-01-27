#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaMiscTopology" for configuration "MinSizeRel"
set_property(TARGET SofaMiscTopology APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaMiscTopology PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaMiscTopology.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaMiscTopology.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaMiscTopology )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaMiscTopology "${_IMPORT_PREFIX}/lib/SofaMiscTopology.lib" "${_IMPORT_PREFIX}/bin/SofaMiscTopology.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
