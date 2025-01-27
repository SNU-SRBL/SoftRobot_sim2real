#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Visual" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Visual APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Visual PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Visual.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_MINSIZEREL "tinyxml"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Visual.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Visual )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Visual "${_IMPORT_PREFIX}/lib/Sofa.Component.Visual.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Visual.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
