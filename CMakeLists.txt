cmake_minimum_required(VERSION 3.20)

project(project LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_CLANG_TIDY "clang-tidy;-checks=performance-*,bugprone-*")

add_executable(project src/main.cpp)

set_target_properties(project PROPERTIES 
  RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)

include(FetchContent)

FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG v1.13.0
)
#FetchContent_MakeAvailable(googletest)
#target_link_libraries(tests GTest::gtest_main)
#enable_testing()
#include(GoogleTest)
#gtest_discover_tests(tests)
