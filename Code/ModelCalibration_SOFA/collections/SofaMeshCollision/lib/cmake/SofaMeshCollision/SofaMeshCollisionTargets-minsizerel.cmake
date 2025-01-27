#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaMeshCollision" for configuration "MinSizeRel"
set_property(TARGET SofaMeshCollision APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaMeshCollision PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaMeshCollision.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaMeshCollision.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaMeshCollision )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaMeshCollision "${_IMPORT_PREFIX}/lib/SofaMeshCollision.lib" "${_IMPORT_PREFIX}/bin/SofaMeshCollision.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
