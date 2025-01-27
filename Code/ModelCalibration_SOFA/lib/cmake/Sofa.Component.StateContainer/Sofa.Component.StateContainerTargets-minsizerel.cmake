#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.StateContainer" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.StateContainer APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.StateContainer PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.StateContainer.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.StateContainer.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.StateContainer )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.StateContainer "${_IMPORT_PREFIX}/lib/Sofa.Component.StateContainer.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.StateContainer.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
