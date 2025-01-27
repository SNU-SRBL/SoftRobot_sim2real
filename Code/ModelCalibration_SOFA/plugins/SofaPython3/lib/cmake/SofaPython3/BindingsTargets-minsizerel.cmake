#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaPython3::Bindings.Sofa.Tests" for configuration "MinSizeRel"
set_property(TARGET SofaPython3::Bindings.Sofa.Tests APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaPython3::Bindings.Sofa.Tests PROPERTIES
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Bindings.Sofa.Tests.exe"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaPython3::Bindings.Sofa.Tests )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaPython3::Bindings.Sofa.Tests "${_IMPORT_PREFIX}/bin/Bindings.Sofa.Tests.exe" )

# Import target "SofaPython3::Bindings.SofaRuntime.Tests" for configuration "MinSizeRel"
set_property(TARGET SofaPython3::Bindings.SofaRuntime.Tests APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaPython3::Bindings.SofaRuntime.Tests PROPERTIES
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Bindings.SofaRuntime.Tests.exe"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaPython3::Bindings.SofaRuntime.Tests )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaPython3::Bindings.SofaRuntime.Tests "${_IMPORT_PREFIX}/bin/Bindings.SofaRuntime.Tests.exe" )

# Import target "SofaPython3::Bindings.SofaTypes.Tests" for configuration "MinSizeRel"
set_property(TARGET SofaPython3::Bindings.SofaTypes.Tests APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaPython3::Bindings.SofaTypes.Tests PROPERTIES
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Bindings.SofaTypes.Tests.exe"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaPython3::Bindings.SofaTypes.Tests )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaPython3::Bindings.SofaTypes.Tests "${_IMPORT_PREFIX}/bin/Bindings.SofaTypes.Tests.exe" )

# Import target "SofaPython3::Bindings.Modules.Tests" for configuration "MinSizeRel"
set_property(TARGET SofaPython3::Bindings.Modules.Tests APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaPython3::Bindings.Modules.Tests PROPERTIES
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Bindings.Modules.Tests.exe"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaPython3::Bindings.Modules.Tests )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaPython3::Bindings.Modules.Tests "${_IMPORT_PREFIX}/bin/Bindings.Modules.Tests.exe" )

# Import target "SofaPython3::CosseratBindings" for configuration "MinSizeRel"
set_property(TARGET SofaPython3::CosseratBindings APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaPython3::CosseratBindings PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/python3/site-packages/CosseratPlugin.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_MINSIZEREL "Python::Python"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/lib/python3/site-packages/CosseratPlugin.cp38-win_amd64.pyd"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaPython3::CosseratBindings )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaPython3::CosseratBindings "${_IMPORT_PREFIX}/lib/python3/site-packages/CosseratPlugin.lib" "${_IMPORT_PREFIX}/lib/python3/site-packages/CosseratPlugin.cp38-win_amd64.pyd" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
