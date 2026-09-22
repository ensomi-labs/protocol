// swift-tools-version: 6.0

import PackageDescription

let package = Package(
    name: "EnsomiProtocol",
    products: [
        .library(
            name: "EnsomiProtocol",
            targets: ["EnsomiProtocol"]
        )
    ],
    dependencies: [
        .package(
            url: "https://github.com/apple/swift-protobuf.git",
            from: "1.38.0"
        )
    ],
    targets: [
        .target(
            name: "EnsomiProtocol",
            dependencies: [
                .product(name: "SwiftProtobuf", package: "swift-protobuf")
            ],
            path: "gen/swift",
            sources: [
                "ensomi/protocol/v1/core.pb.swift",
                "ensomi/protocol/v1/envelope.pb.swift",
                "ensomi/protocol/v1/inference.pb.swift",
                "ensomi/protocol/v1/mapper.pb.swift",
            ]
        )
    ]
)
