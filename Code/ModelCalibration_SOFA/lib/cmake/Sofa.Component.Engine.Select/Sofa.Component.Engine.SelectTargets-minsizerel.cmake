#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Engine.Select" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Engine.Select APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Engine.Select PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Engine.Select.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Engine.Select.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Engine.Select )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Engine.Select "${_IMPORT_PREFIX}/lib/Sofa.Component.Engine.Select.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Engine.Select.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
