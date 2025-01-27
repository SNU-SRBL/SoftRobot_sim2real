#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaObjectInteraction" for configuration "MinSizeRel"
set_property(TARGET SofaObjectInteraction APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaObjectInteraction PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaObjectInteraction.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaObjectInteraction.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaObjectInteraction )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaObjectInteraction "${_IMPORT_PREFIX}/lib/SofaObjectInteraction.lib" "${_IMPORT_PREFIX}/bin/SofaObjectInteraction.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
