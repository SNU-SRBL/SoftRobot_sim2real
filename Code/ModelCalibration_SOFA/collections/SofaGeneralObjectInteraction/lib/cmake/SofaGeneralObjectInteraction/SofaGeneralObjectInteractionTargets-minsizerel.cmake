#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaGeneralObjectInteraction" for configuration "MinSizeRel"
set_property(TARGET SofaGeneralObjectInteraction APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaGeneralObjectInteraction PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaGeneralObjectInteraction.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaGeneralObjectInteraction.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaGeneralObjectInteraction )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaGeneralObjectInteraction "${_IMPORT_PREFIX}/lib/SofaGeneralObjectInteraction.lib" "${_IMPORT_PREFIX}/bin/SofaGeneralObjectInteraction.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
