#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaPhysicsAPI" for configuration "MinSizeRel"
set_property(TARGET SofaPhysicsAPI APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaPhysicsAPI PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaPhysicsAPI.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaPhysicsAPI.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaPhysicsAPI )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaPhysicsAPI "${_IMPORT_PREFIX}/lib/SofaPhysicsAPI.lib" "${_IMPORT_PREFIX}/bin/SofaPhysicsAPI.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
