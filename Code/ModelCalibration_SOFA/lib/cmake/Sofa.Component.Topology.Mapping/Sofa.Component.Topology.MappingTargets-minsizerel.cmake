#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Topology.Mapping" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Topology.Mapping APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Topology.Mapping PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Topology.Mapping.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Topology.Mapping.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Topology.Mapping )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Topology.Mapping "${_IMPORT_PREFIX}/lib/Sofa.Component.Topology.Mapping.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Topology.Mapping.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
