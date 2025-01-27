#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Engine.Analyze" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Engine.Analyze APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Engine.Analyze PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Engine.Analyze.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Engine.Analyze.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Engine.Analyze )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Engine.Analyze "${_IMPORT_PREFIX}/lib/Sofa.Component.Engine.Analyze.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Engine.Analyze.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
