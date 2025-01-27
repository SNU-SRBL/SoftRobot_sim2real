#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaTopologyMapping" for configuration "MinSizeRel"
set_property(TARGET SofaTopologyMapping APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaTopologyMapping PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaTopologyMapping.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaTopologyMapping.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaTopologyMapping )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaTopologyMapping "${_IMPORT_PREFIX}/lib/SofaTopologyMapping.lib" "${_IMPORT_PREFIX}/bin/SofaTopologyMapping.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
