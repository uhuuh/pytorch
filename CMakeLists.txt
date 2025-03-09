cmake_minimum_required(VERSION 3.10)
project(torch LANGUAGES C CXX)

FilE(GLOB_RECURSE
    SOURCE_FILES
    ./*.cpp
)

include_directories(
    .
    ./aten/src
)

#add_compile_definitions(ENABLE_CPU)
#add_compile_definitions(ENABLE_GPU)

add_library(test ${SOURCE_FILES})