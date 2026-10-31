# Release Notes

## Latest changes

## 1.3.0

Fix transaction size calculation breaking in future Python versions: bytes fields are now encoded as URL-safe Base64, as protobuf expects

Support python 3.15 and free-threaded python

Drop python 3.10 support

Require protobuf 3.20+

Fix the usage example in README, slimmer sdist package

## 1.2.0

Support Python 3.14

Require Python 3.10+

Switch to github actions, releases are now uploaded via Trusted Publishing.

## 1.1.1

Support Python 3.13

## 1.1.0

Use uv & ruff as build infrastructure

Require Python 3.9+

## 1.0.6

Don't install a separate tests package, but include tests in source tarball

## 1.0.5

Rename BitcartCC to Bitcart

## 1.0.4

Re-generate protobuf files with the latest protoc

## 1.0.3

Support Python 3.11

## 1.0.2

Take deep copy of tx passed

## 1.0.1

Use older protobuf compiler for now

## 1.0.0

Initial release
