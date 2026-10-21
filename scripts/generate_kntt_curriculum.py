import json

# Script tạo cơ sở dữ liệu chương trình chuẩn SGK Kết nối tri thức (KNTT)
# cho 4 khối lớp 6, 7, 8, 9

kntt_data = {
    6: {
        "ten_khoi": "Tin học Lớp 6",
        "bo_sach": "Kết nối tri thức với cuộc sống",
        "ky_kiem_tra": {
            "Giữa kỳ 1": ["Bài 1: Thông tin và dữ liệu", "Bài 2: Xử lí thông tin", "Bài 3: Thông tin trong máy tính", "Bài 4: Mạng máy tính"],
            "Cuối kỳ 1": ["Bài 1: Thông tin và dữ liệu", "Bài 2: Xử lí thông tin", "Bài 3: Thông tin trong máy tính", "Bài 4: Mạng máy tính", "Bài 5: Internet", "Bài 6: Mạng thông tin toàn cầu", "Bài 7: Tìm kiếm thông tin trên Internet", "Bài 8: Thư điện tử"],
            "Giữa kỳ 2": ["Bài 9: An toàn thông tin trên Internet", "Bài 10: Sơ đồ tư duy", "Bài 11: Định dạng văn bản", "Bài 12: Trình bày thông tin ở dạng bảng", "Bài 13: Thực hành: Tìm kiếm và thay thế"],
            "Cuối kỳ 2": ["Bài 10: Sơ đồ tư duy", "Bài 11: Định dạng văn bản", "Bài 12: Trình bày thông tin ở dạng bảng", "Bài 14: Thực hành tổng hợp: Hoàn thiện Sổ lưu niệm", "Bài 15: Thuật toán", "Bài 16: Các cấu trúc điều khiển", "Bài 17: Chương trình máy tính"]
        },
        "chu_de": {
            "Chủ đề 1. Máy tính và cộng đồng": {
                "ten": "Máy tính và cộng đồng",
                "noi_dung": {
                    "Bài 1: Thông tin và dữ liệu": {
                        "biet": [
                            "Nêu được ví dụ về thông tin và dữ liệu thu nhận được từ các giác quan của con người.",
                            "Nhận biết được vai trò của thông tin trong đời sống hàng ngày."
                        ],
                        "hieu": [
                            "Giải thích được mối quan hệ và sự khác nhau giữa thông tin và vật mang tin.",
                            "Nêu được ví dụ minh họa về thông tin giúp con người đưa ra quyết định đúng đắn."
                        ],
                        "van_dung": [
                            "Phân tích được một tình huống thực tiễn để xác định chính xác đâu là thông tin, dữ liệu và vật mang tin."
                        ]
                    },
                    "Bài 2: Xử lí thông tin": {
                        "biet": [
                            "Nêu được 4 bước cơ bản trong quy trình xử lí thông tin: Thu nhận, Lưu trữ, Xử lí và Truyền tải thông tin.",
                            "Nhận biết được các thiết bị máy tính thực hiện các bước xử lí thông tin."
                        ],
                        "hieu": [
                            "Giải thích được máy tính là công cụ hỗ trợ con người xử lí thông tin nhanh chóng và chuẩn xác.",
                            "Mô tả được hoạt động xử lí thông tin của bộ não con người và so sánh với máy tính."
                        ],
                        "van_dung": [
                            "Xác định được các thao tác xử lí thông tin trong một bài toán học tập thực tế (ví dụ: làm bài tập môn Toán, vẽ sơ đồ)."
                        ]
                    },
                    "Bài 3: Thông tin trong máy tính": {
                        "biet": [
                            "Biết máy tính chỉ hiểu và xử lí dãy bit gồm hai ký hiệu 0 và 1.",
                            "Kể tên được các đơn vị đo dung lượng thông tin: Bit, Byte, KB, MB, GB, TB."
                        ],
                        "hieu": [
                            "Giải thích được cách biểu diễn văn bản, số, hình ảnh, âm thanh thành dãy bit trong máy tính.",
                            "Quy đổi được giữa các đơn vị đo dung lượng thông tin thông dụng (1 Byte = 8 bit, 1 KB = 1024 Byte)."
                        ],
                        "van_dung": [
                            "Tính toán được dung lượng bộ nhớ thiết bị (USB, thẻ nhớ) để chứa số lượng tệp tin bài học, ảnh chụp thực tế."
                        ]
                    }
                }
            },
            "Chủ đề 2. Mạng máy tính và Internet": {
                "ten": "Mạng máy tính và Internet",
                "noi_dung": {
                    "Bài 4: Mạng máy tính": {
                        "biet": [
                            "Nêu được khái niệm mạng máy tính và lợi ích cơ bản của mạng máy tính.",
                            "Kể tên được các thành phần chính của mạng: thiết bị đầu cuối, thiết bị kết nối (Switch, Modem, Router) và đường truyền."
                        ],
                        "hieu": [
                            "Phân biệt được mạng có dây (sử dụng cáp mạng) và mạng không dây (sử dụng sóng Wi-Fi).",
                            "Trình bày được ưu điểm của việc kết nối mạng trong chia sẻ dữ liệu và thiết bị phần cứng (máy in)."
                        ],
                        "van_dung": [
                            "Mô tả được mô hình kết nối các thiết bị (máy tính, điện thoại, máy in) trong gia đình hoặc phòng thực hành Tin học."
                        ]
                    },
                    "Bài 5: Internet": {
                        "biet": [
                            "Nêu được định nghĩa Internet là mạng kết nối hàng triệu máy tính trên toàn thế giới.",
                            "Kể tên được một số dịch vụ phổ biến trên Internet: tra cứu thông tin, học trực tuyến, giải trí, thư điện tử."
                        ],
                        "hieu": [
                            "Giải thích được đặc điểm không có ai là chủ sở hữu duy nhất của mạng Internet.",
                            "Trình bày được lợi ích to lớn và những nguy cơ tiềm ẩn khi sử dụng Internet."
                        ],
                        "van_dung": [
                            "Khai thác được thông tin từ Internet để phục vụ một nhiệm vụ học tập trên lớp."
                        ]
                    }
                }
            },
            "Chủ đề 3. Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin": {
                "ten": "Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin",
                "noi_dung": {
                    "Bài 6: Mạng thông tin toàn cầu": {
                        "biet": [
                            "Nêu được khái niệm World Wide Web (WWW), website, trang chủ, địa chỉ trang web (URL).",
                            "Kể tên được một số trình duyệt web phổ biến: Google Chrome, Microsoft Edge, Mozilla Firefox, Cốc Cốc."
                        ],
                        "hieu": [
                            "Hiểu được siêu văn bản và siêu liên kết (hyperlink) giúp kết nối các tài liệu trên mạng.",
                            "Trình bày được các bước truy cập vào một trang web bằng địa chỉ cho trước."
                        ],
                        "van_dung": [
                            "Sử dụng trình duyệt web truy cập thành thạo trang tin tức học đường hoặc Cổng thông tin Bộ GD&ĐT."
                        ]
                    },
                    "Bài 7: Tìm kiếm thông tin trên Internet": {
                        "biet": [
                            "Nêu được công dụng của máy tìm kiếm (Google, Bing) và khái niệm từ khóa tìm kiếm.",
                            "Nhận biết được danh sách kết quả trả về từ máy tìm kiếm."
                        ],
                        "hieu": [
                            "Giải thích được việc lựa chọn từ khóa chính xác giúp tìm kiếm thông tin nhanh chóng và hiệu quả.",
                            "Phân biệt được thông tin chính xác và thông tin chưa được kiểm chứng trên mạng."
                        ],
                        "van_dung": [
                            "Sử dụng kết hợp các từ khóa thu hẹp phạm vi để tìm tài liệu học tập một cách tối ưu."
                        ]
                    },
                    "Bài 8: Thư điện tử": {
                        "biet": [
                            "Nêu được khái niệm thư điện tử (email) và cấu trúc của một địa chỉ email chuẩn (tên_người_dùng@tên_miền).",
                            "Biết các thành phần của hộp thư điện tử: Hộp thư đến, Thư đã gửi, Thùng rác."
                        ],
                        "hieu": [
                            "Giải thích được các ưu điểm của thư điện tử so với thư truyền thống (tốc độ tức thời, tiết kiệm, gửi tệp đính kèm).",
                            "Phân biệt được tiêu đề thư, nội dung thư và tệp đính kèm."
                        ],
                        "van_dung": [
                            "Soạn và gửi được một email hoàn chỉnh có tệp bài tập đính kèm gửi thầy cô giáo hoặc bạn bè."
                        ]
                    }
                }
            },
            "Chủ đề 4. Đạo đức, pháp luật và văn hóa trong môi trường số": {
                "ten": "Đạo đức, pháp luật và văn hóa trong môi trường số",
                "noi_dung": {
                    "Bài 9: An toàn thông tin trên Internet": {
                        "biet": [
                            "Nhận biết được tầm quan trọng của việc bảo vệ thông tin cá nhân và tài khoản trên không gian mạng.",
                            "Kể tên được các nguy cơ khi dùng Internet: virus máy tính, lừa đảo trực tuyến, thông tin độc hại."
                        ],
                        "hieu": [
                            "Giải thích được tác hại của việc tiết lộ mật khẩu, thông tin riêng tư cho người lạ trên mạng.",
                            "Nêu được quy tắc đặt mật khẩu mạnh (gồm chữ hoa, chữ thường, số và ký tự đặc biệt)."
                        ],
                        "van_dung": [
                            "Thực hành tạo lập mật khẩu mạnh và có ý thức cảnh giác trước các đường link lạ trên mạng."
                        ]
                    }
                }
            },
            "Chủ đề 5. Ứng dụng tin học": {
                "ten": "Ứng dụng tin học",
                "noi_dung": {
                    "Bài 10: Sơ đồ tư duy": {
                        "biet": [
                            "Nêu được khái niệm sơ đồ tư duy và các thành phần chính: chủ đề chính, nhánh chính, nhánh phụ, từ khóa.",
                            "Biết công dụng của sơ đồ tư duy trong việc ghi nhớ và tóm tắt kiến thức."
                        ],
                        "hieu": [
                            "Trình bày được các bước tóm tắt nội dung một bài học dưới dạng sơ đồ tư duy.",
                            "Giải thích được lợi ích của việc sử dụng màu sắc, hình ảnh trực quan trong sơ đồ tư duy."
                        ],
                        "van_dung": [
                            "Vẽ được một sơ đồ tư duy hoàn chỉnh (bằng tay hoặc phần mềm) để ôn tập một chủ đề kiến thức."
                        ]
                    },
                    "Bài 11: Định dạng văn bản": {
                        "biet": [
                            "Nhận biết được các thành phần của văn bản: ký tự, từ, câu, đoạn văn bản, trang.",
                            "Kể tên được các lệnh định dạng ký tự (phông chữ, cỡ chữ, kiểu chữ, màu chữ) và định dạng đoạn (căn lề, giãn dòng)."
                        ],
                        "hieu": [
                            "Hiểu được quy tắc gõ chữ tiếng Việt theo chuẩn Telex hoặc Vni.",
                            "Phân biệt được định dạng ký tự và định dạng đoạn văn bản."
                        ],
                        "van_dung": [
                            "Soạn thảo và căn chỉnh định dạng một văn bản hoàn chỉnh đảm bảo tính thẩm mỹ và đúng thể thức."
                        ]
                    },
                    "Bài 12: Trình bày thông tin ở dạng bảng": {
                        "biet": [
                            "Biết các thao tác tạo bảng, chèn thêm hoặc xóa bớt hàng, cột trong phần mềm soạn thảo.",
                            "Nhận biết cấu trúc bảng gồm hàng, cột và các ô tính."
                        ],
                        "hieu": [
                            "Giải thích được ưu điểm của việc trình bày thông tin ở dạng bảng so với văn bản thông thường.",
                            "Hiểu cách căn chỉnh lề nội dung trong ô và thay đổi độ rộng cột, chiều cao hàng."
                        ],
                        "van_dung": [
                            "Tạo lập được bảng Thời khóa biểu hoặc Bảng điểm học tập cá nhân rõ ràng, đẹp mắt."
                        ]
                    },
                    "Bài 13: Thực hành: Tìm kiếm và thay thế": {
                        "biet": [
                            "Biết công dụng và cách mở công cụ Tìm kiếm (Find) và Thay thế (Replace) trong phần mềm soạn thảo."
                        ],
                        "hieu": [
                            "Hiểu được sự khác nhau giữa lệnh Tìm kiếm (chỉ định vị từ khóa) và Thay thế (sửa đổi nội dung).",
                            "Trình bày được cách thức thay thế hàng loạt từ khóa trong toàn bộ tài liệu."
                        ],
                        "van_dung": [
                            "Sử dụng thành thạo công cụ Find and Replace để sửa lỗi chính tả hàng loạt trong văn bản dài."
                        ]
                    },
                    "Bài 14: Thực hành tổng hợp: Hoàn thiện Sổ lưu niệm": {
                        "biet": [
                            "Biết cách chèn hình ảnh, tạo viền trang, đánh số trang cho văn bản."
                        ],
                        "hieu": [
                            "Giải thích được cách bố trí hình ảnh hài hòa bên cạnh đoạn văn bản."
                        ],
                        "van_dung": [
                            "Hoàn thiện một sản phẩm số dạng tập san/sổ lưu niệm có tiêu đề, hình ảnh minh họa, bảng biểu sinh động."
                        ]
                    }
                }
            },
            "Chủ đề 6. Giải quyết vấn đề với sự trợ giúp của máy tính": {
                "ten": "Giải quyết vấn đề với sự trợ giúp của máy tính",
                "noi_dung": {
                    "Bài 15: Thuật toán": {
                        "biet": [
                            "Nêu được khái niệm thuật toán là dãy các thao tác tuần tự để giải quyết một nhiệm vụ cho trước.",
                            "Biết hai cách mô tả thuật toán: Liệt kê các bước bằng ngôn ngữ tự nhiên và Sơ đồ khối."
                        ],
                        "hieu": [
                            "Giải thích được ý nghĩa các hình khối chuẩn trong sơ đồ khối (hình elip: Bắt đầu/Kết thúc; hình chữ nhật: Xử lý; hình thoi: Điều kiện rẽ nhánh; hình bình hành: Vào/Ra).",
                            "Xác định được đầu vào (Input) và đầu ra (Output) của một thuật toán cụ thể."
                        ],
                        "van_dung": [
                            "Vẽ được sơ đồ khối mô tả thuật toán giải một bài toán thực tế đơn giản (ví dụ: pha trà, tìm số lớn hơn trong hai số)."
                        ]
                    },
                    "Bài 16: Các cấu trúc điều khiển": {
                        "biet": [
                            "Nêu được 3 cấu trúc điều khiển cơ bản trong thuật toán: Tuần tự, Rẽ nhánh (nếu... thì...) và Lặp."
                        ],
                        "hieu": [
                            "Phân biệt được cấu trúc rẽ nhánh dạng thiếu (Nếu... thì) và dạng đủ (Nếu... thì... nếu không thì...).",
                            "Hiểu được nguyên lý hoạt động của cấu trúc lặp với số lần biết trước hoặc lặp có điều kiện."
                        ],
                        "van_dung": [
                            "Mô tả được thuật toán có sử dụng cấu trúc rẽ nhánh hoặc lặp để giải quyết tình huống thực tế."
                        ]
                    },
                    "Bài 17: Chương trình máy tính": {
                        "biet": [
                            "Nêu được khái niệm chương trình máy tính là tập hợp các lệnh viết bằng ngôn ngữ lập trình.",
                            "Biết vai trò của ngôn ngữ lập trình trực quan (như Scratch) giúp học sinh làm quen với thuật toán."
                        ],
                        "hieu": [
                            "Hiểu được máy tính thực hiện các câu lệnh trong chương trình một cách tuần tự và tự động."
                        ],
                        "van_dung": [
                            "Đọc hiểu được kịch bản chương trình đơn giản và dự đoán được kết quả hiển thị trên màn hình."
                        ]
                    }
                }
            }
        }
    },
    7: {
        "ten_khoi": "Tin học Lớp 7",
        "bo_sach": "Kết nối tri thức với cuộc sống",
        "ky_kiem_tra": {
            "Giữa kỳ 1": ["Bài 1: Thiết bị vào - ra", "Bài 2: Phần mềm máy tính", "Bài 3: Quản lí dữ liệu trong máy tính", "Bài 4: Mạng xã hội và một số kênh trao đổi thông tin trên Internet"],
            "Cuối kỳ 1": ["Bài 1: Thiết bị vào - ra", "Bài 2: Phần mềm máy tính", "Bài 3: Quản lí dữ liệu trong máy tính", "Bài 4: Mạng xã hội và một số kênh trao đổi thông tin trên Internet", "Bài 5: Ứng xử trên mạng", "Bài 6: Làm quen với phần mềm bảng tính", "Bài 7: Tính toán tự động trên bảng tính", "Bài 8: Công cụ hỗ trợ tính toán"],
            "Giữa kỳ 2": ["Bài 9: Trình bày bảng tính", "Bài 10: Hoàn thiện bảng tính", "Bài 11: Tạo bài trình chiếu", "Bài 12: Sử dụng ảnh minh họa, hiệu ứng động trong bài trình chiếu", "Bài 13: Thực hành tổng hợp: Hoàn thiện bài trình chiếu"],
            "Cuối kỳ 2": ["Bài 9: Trình bày bảng tính", "Bài 10: Hoàn thiện bảng tính", "Bài 11: Tạo bài trình chiếu", "Bài 14: Thuật toán tìm kiếm tuần tự", "Bài 15: Thuật toán tìm kiếm nhị phân", "Bài 16: Thuật toán sắp xếp"]
        },
        "chu_de": {
            "Chủ đề 1. Máy tính và cộng đồng": {
                "ten": "Máy tính và cộng đồng",
                "noi_dung": {
                    "Bài 1: Thiết bị vào - ra": {
                        "biet": [
                            "Kể tên và phân loại được các thiết bị vào (bàn phím, chuột, micro, máy quét) và thiết bị ra (màn hình, máy in, loa, máy chiếu).",
                            "Biết các cổng kết nối thông dụng: USB, HDMI, Type-C, Jack 3.5mm."
                        ],
                        "hieu": [
                            "Giải thích được chức năng trao đổi dữ liệu giữa thiết bị vào/ra với thân máy tính.",
                            "Hiểu được sự cần thiết của các thiết bị vào - ra chuyên dụng cho người khuyết tật."
                        ],
                        "van_dung": [
                            "Thao tác gắn và tháo thiết bị ngoại vi (chuột, USB, tai nghe) an toàn trên máy tính."
                        ]
                    },
                    "Bài 2: Phần mềm máy tính": {
                        "biet": [
                            "Nêu được chức năng cơ bản của hệ điều hành và phần mềm ứng dụng.",
                            "Kể tên được một số hệ điều hành phổ biến (Windows, Linux, macOS, Android, iOS)."
                        ],
                        "hieu": [
                            "Phân biệt được hệ điều hành (quản lý phần cứng, cung cấp môi trường) và phần mềm ứng dụng (giải quyết công việc cụ thể).",
                            "Mô tả được mối quan hệ phối hợp giữa người dùng, phần mềm ứng dụng, hệ điều hành và phần cứng."
                        ],
                        "van_dung": [
                            "Lựa chọn và cài đặt phần mềm ứng dụng phù hợp với nhu cầu học tập và hệ điều hành của máy."
                        ]
                    },
                    "Bài 3: Quản lí dữ liệu trong máy tính": {
                        "biet": [
                            "Nhận biết được tên tệp, phần mở rộng của tệp và cấu trúc thư mục dạng cây phân cấp.",
                            "Biết các thao tác quản lý tệp và thư mục: tạo mới, đổi tên, sao chép, di chuyển, xóa."
                        ],
                        "hieu": [
                            "Giải thích được sự cần thiết của việc tổ chức lưu trữ dữ liệu khoa học, hợp lý.",
                            "Phân biệt được các dạng tệp tin thông dụng qua phần mở rộng (.docx, .xlsx, .pptx, .pdf, .mp3, .mp4)."
                        ],
                        "van_dung": [
                            "Xây dựng được cây thư mục khoa học để lưu trữ bài học các môn trên máy tính cá nhân."
                        ]
                    }
                }
            },
            "Chủ đề 2. Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin": {
                "ten": "Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin",
                "noi_dung": {
                    "Bài 4: Mạng xã hội và một số kênh trao đổi thông tin trên Internet": {
                        "biet": [
                            "Kể tên được các kênh trao đổi thông tin trên Internet: mạng xã hội, diễn đàn, ứng dụng trò chuyện trực tuyến.",
                            "Biết các tính năng cơ bản của mạng xã hội: tạo hồ sơ, kết bạn, chia sẻ thông tin, tương tác."
                        ],
                        "hieu": [
                            "Trình bày được ưu điểm và hạn chế của việc giao tiếp qua mạng xã hội so với giao tiếp trực tiếp.",
                            "Nêu được những mặt trái và rủi ro tiềm ẩn khi tham gia mạng xã hội."
                        ],
                        "van_dung": [
                            "Sử dụng mạng xã hội một cách an toàn, lành mạnh để trao đổi học tập và kết nối bạn bè."
                        ]
                    }
                }
            },
            "Chủ đề 3. Đạo đức, pháp luật và văn hóa trong môi trường số": {
                "ten": "Đạo đức, pháp luật và văn hóa trong môi trường số",
                "noi_dung": {
                    "Bài 5: Ứng xử trên mạng": {
                        "biet": [
                            "Nêu được các quy định cơ bản về ứng xử văn minh và tôn trọng quyền riêng tư trên không gian mạng.",
                            "Nhận biết được các hành vi vi phạm đạo đức, pháp luật: phát tán thông tin giả, xúc phạm nhân phẩm người khác."
                        ],
                        "hieu": [
                            "Giải thích được tác hại của hiện tượng bắt nạt trên mạng (cyberbullying) và tin giả (fake news).",
                            "Biết cách tự bảo vệ mình và tìm kiếm sự giúp đỡ từ thầy cô, cha mẹ khi bị đe dọa trên mạng."
                        ],
                        "van_dung": [
                            "Thực hiện giao tiếp, bình luận lịch sự, chuẩn mực và tôn trọng bản quyền khi chia sẻ tài liệu."
                        ]
                    }
                }
            },
            "Chủ đề 4. Ứng dụng tin học": {
                "ten": "Ứng dụng tin học",
                "noi_dung": {
                    "Bài 6: Làm quen với phần mềm bảng tính": {
                        "biet": [
                            "Nhận biết được giao diện của phần mềm bảng tính: thanh tiêu đề, thanh công thức, ô, hàng, cột, trang tính.",
                            "Nhận biết địa chỉ ô, khối ô và các kiểu dữ liệu cơ bản: số, ký tự, ngày tháng."
                        ],
                        "hieu": [
                            "Hiểu được cách nhập, chỉnh sửa dữ liệu và di chuyển con trỏ trong bảng tính.",
                            "Phân biệt được cách căn lề mặc định của dữ liệu số (bên phải) và dữ liệu ký tự (bên trái)."
                        ],
                        "van_dung": [
                            "Tạo lập được trang tính đơn giản chứa danh sách học sinh hoặc bảng điểm của tổ."
                        ]
                    },
                    "Bài 7: Tính toán tự động trên bảng tính": {
                        "biet": [
                            "Biết công thức trong bảng tính luôn bắt đầu bằng dấu bằng '='.",
                            "Kể tên được các phép toán số học cơ bản: cộng (+), trừ (-), nhân (*), chia (/), lũy thừa (^)."
                        ],
                        "hieu": [
                            "Giải thích được lợi ích của việc sử dụng địa chỉ ô trong công thức để tự động tính toán lại khi dữ liệu thay đổi.",
                            "Hiểu được sự thay đổi của địa chỉ tương đối khi thực hiện sao chép công thức sang ô khác."
                        ],
                        "van_dung": [
                            "Viết đúng công thức chứa địa chỉ ô để tính tổng điểm, điểm trung bình cho bảng số liệu thực tế."
                        ]
                    },
                    "Bài 8: Công cụ hỗ trợ tính toán": {
                        "biet": [
                            "Kể tên và biết công dụng của các hàm tính toán cơ bản: SUM (tính tổng), AVERAGE (trung bình), COUNT (đếm số lượng), MAX (lớn nhất), MIN (nhỏ nhất).",
                            "Biết cú pháp chuẩn của hàm: Tên_hàm(Danh_sách_đối_số)."
                        ],
                        "hieu": [
                            "Hiểu cách chọn danh sách đối số là các ô hoặc khối ô liền kề trong bảng tính.",
                            "Phân biệt được cách dùng dấu phẩy (,) hoặc dấu hai chấm (:) khi khai báo khối dữ liệu cho hàm."
                        ],
                        "van_dung": [
                            "Sử dụng kết hợp các hàm SUM, AVERAGE, MAX, MIN để xử lý bảng điểm tổng kết học kỳ."
                        ]
                    },
                    "Bài 9: Trình bày bảng tính": {
                        "biet": [
                            "Biết các thao tác định dạng bảng tính: kẻ đường viền, tô màu nền ô, gộp ô (Merge & Center).",
                            "Biết định dạng hiển thị dữ liệu số: số thập phân, phần trăm (%), dấu phân cách hàng nghìn."
                        ],
                        "hieu": [
                            "Giải thích được ý nghĩa của việc trình bày bảng tính rõ ràng, có thẩm mỹ giúp người đọc dễ theo dõi."
                        ],
                        "van_dung": [
                            "Định dạng hoàn chỉnh một bảng thống kê chi tiêu hoặc bảng điểm lớp học chuyên nghiệp."
                        ]
                    },
                    "Bài 10: Hoàn thiện bảng tính": {
                        "biet": [
                            "Biết thao tác sắp xếp dữ liệu tăng dần/giảm dần và lọc dữ liệu tự động (AutoFilter) trong bảng tính."
                        ],
                        "hieu": [
                            "Hiểu được cách chọn tiêu chí sắp xếp và điều kiện lọc để trích xuất danh sách cần tìm kiếm."
                        ],
                        "van_dung": [
                            "Sắp xếp bảng điểm theo thứ tự giảm dần và lọc ra danh sách học sinh đạt danh hiệu Xuất sắc."
                        ]
                    },
                    "Bài 11: Tạo bài trình chiếu": {
                        "biet": [
                            "Nêu được vai trò của bài trình chiếu và kể tên các thành phần cơ bản của phần mềm trình chiếu (PowerPoint).",
                            "Biết cách chèn thêm trang chiếu mới, chọn bố cục (layout) và nhập văn bản vào hộp chứa văn bản (placeholder)."
                        ],
                        "hieu": [
                            "Trình bày được các bước cơ bản để thiết kế một bài trình chiếu phục vụ báo cáo thuyết trình."
                        ],
                        "van_dung": [
                            "Tạo được bài trình chiếu 3-5 trang giới thiệu về bản thân hoặc một chủ đề bài học."
                        ]
                    },
                    "Bài 12: Sử dụng ảnh minh họa, hiệu ứng động trong bài trình chiếu": {
                        "biet": [
                            "Biết cách chèn hình ảnh minh họa, biểu tượng vào trang chiếu.",
                            "Biết hai loại hiệu ứng động: hiệu ứng chuyển trang (Transition) và hiệu ứng cho đối tượng (Animation)."
                        ],
                        "hieu": [
                            "Giải thích được việc sử dụng hiệu ứng động hợp lý giúp bài báo cáo sinh động, tránh lạm dụng gây mất tập trung."
                        ],
                        "van_dung": [
                            "Áp dụng hiệu ứng chuyển trang và hoạt họa nhịp nhàng cho bài thuyết trình."
                        ]
                    },
                    "Bài 13: Thực hành tổng hợp: Hoàn thiện bài trình chiếu": {
                        "biet": [
                            "Biết cách chạy trình chiếu (Slide Show) từ trang đầu hoặc từ trang hiện tại."
                        ],
                        "hieu": [
                            "Hiểu cách điều khiển bài trình chiếu khi báo cáo trước lớp."
                        ],
                        "van_dung": [
                            "Hoàn thiện bài trình chiếu báo cáo dự án học tập có cấu trúc chặt chẽ, hình ảnh hài hòa và hiệu ứng trang nhã."
                        ]
                    }
                }
            },
            "Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính": {
                "ten": "Giải quyết vấn đề với sự trợ giúp của máy tính",
                "noi_dung": {
                    "Bài 14: Thuật toán tìm kiếm tuần tự": {
                        "biet": [
                            "Nêu được bài toán tìm kiếm và ý tưởng của thuật toán tìm kiếm tuần tự (Linear Search).",
                            "Biết thuật toán tuần tự thực hiện so sánh lần lượt từ phần tử đầu tiên đến phần tử cuối cùng."
                        ],
                        "hieu": [
                            "Mô tả được các bước thực hiện thuật toán tìm kiếm tuần tự trên một dãy số hoặc danh sách cụ thể.",
                            "Nhận biết được điều kiện dừng của thuật toán (tìm thấy phần tử hoặc đã duyệt hết danh sách)."
                        ],
                        "van_dung": [
                            "Mô phỏng từng bước thuật toán tìm kiếm tuần tự để tìm một số hoặc một tên học sinh trong danh sách."
                        ]
                    },
                    "Bài 15: Thuật toán tìm kiếm nhị phân": {
                        "biet": [
                            "Nêu được ý tưởng cốt lõi của thuật toán tìm kiếm nhị phân (Binary Search).",
                            "Biết điều kiện bắt buộc để áp dụng tìm kiếm nhị phân: Dãy dữ liệu đã được sắp xếp."
                        ],
                        "hieu": [
                            "Mô tả được nguyên lý chia đôi dãy dữ liệu sau mỗi bước so sánh với phần tử ở giữa.",
                            "Giải thích được vì sao tìm kiếm nhị phân nhanh và hiệu quả hơn tìm kiếm tuần tự khi danh sách lớn."
                        ],
                        "van_dung": [
                            "Thực hiện từng bước thuật toán tìm kiếm nhị phân để tìm giá trị trong một dãy số đã sắp xếp cho trước."
                        ]
                    },
                    "Bài 16: Thuật toán sắp xếp": {
                        "biet": [
                            "Nêu được bài toán sắp xếp dữ liệu tăng dần hoặc giảm dần trong thực tế.",
                            "Biết tên hai thuật toán sắp xếp cơ bản: Sắp xếp nổi bọt (Bubble Sort) và Sắp xếp chọn (Selection Sort)."
                        ],
                        "hieu": [
                            "Mô tả được các bước thực hiện của thuật toán sắp xếp nổi bọt (đổi chỗ 2 phần tử kề nhau) và sắp xếp chọn (chọn phần tử nhỏ nhất đưa về đầu dãy).",
                            "Giải thích được ý nghĩa của việc sắp xếp dữ liệu giúp công việc tìm kiếm nhanh hơn."
                        ],
                        "van_dung": [
                            "Mô phỏng quá trình sắp xếp một dãy gồm 5 số tự nhiên theo thứ tự tăng dần bằng thuật toán đã học."
                        ]
                    }
                }
            }
        }
    },
    8: {
        "ten_khoi": "Tin học Lớp 8",
        "bo_sach": "Kết nối tri thức với cuộc sống",
        "ky_kiem_tra": {
            "Giữa kỳ 1": ["Bài 1: Lược sử công cụ tính toán", "Bài 2: Thông tin trong môi trường số", "Bài 3: Thực hành: Khai thác thông tin số", "Bài 4: Đạo đức và văn hóa trong sử dụng công nghệ kĩ thuật số"],
            "Cuối kỳ 1": ["Bài 1: Lược sử công cụ tính toán", "Bài 2: Thông tin trong môi trường số", "Bài 3: Thực hành: Khai thác thông tin số", "Bài 4: Đạo đức và văn hóa trong sử dụng công nghệ kĩ thuật số", "Bài 5: Sử dụng bảng tính giải quyết bài toán thực tế", "Bài 6: Sắp xếp và lọc dữ liệu", "Bài 7: Trình bày dữ liệu bằng biểu đồ"],
            "Giữa kỳ 2": ["Bài 8a: Làm việc với danh sách dạng liệt kê và hình ảnh trong văn bản", "Bài 9a: Tạo đầu trang, chân trang cho văn bản", "Bài 10a: Định dạng nâng cao cho trang chiếu", "Bài 11a: Sử dụng bản mẫu tạo bài trình chiếu", "Bài 12: Từ thuật toán đến chương trình"],
            "Cuối kỳ 2": ["Bài 8a: Làm việc với danh sách dạng liệt kê và hình ảnh trong văn bản", "Bài 10a: Định dạng nâng cao cho trang chiếu", "Bài 12: Từ thuật toán đến chương trình", "Bài 13: Biểu diễn dữ liệu", "Bài 14: Cấu trúc điều khiển", "Bài 15: Gỡ lỗi", "Bài 16: Tin học với nghề nghiệp"]
        },
        "chu_de": {
            "Chủ đề 1. Máy tính và cộng đồng": {
                "ten": "Máy tính và cộng đồng",
                "noi_dung": {
                    "Bài 1: Lược sử công cụ tính toán": {
                        "biet": [
                            "Nêu được sơ lược lịch sử phát triển của công cụ tính toán từ bàn tính cơ học đến máy tính điện tử hiện đại.",
                            "Kể tên được 5 thế hệ máy tính điện tử và thành phần điện tử cốt lõi tương ứng (đèn điện tử chân không, bóng bán dẫn, mạch tích hợp, vi xử lý, AI)."
                        ],
                        "hieu": [
                            "Giải thích được xu hướng phát triển của máy tính ngày càng nhỏ gọn, tốc độ xử lý siêu nhanh, tiêu thụ ít năng lượng và thông minh hơn."
                        ],
                        "van_dung": [
                            "Nhận diện và đánh giá được tác động sâu rộng của cuộc cách mạng máy tính đến các lĩnh vực kinh tế - xã hội."
                        ]
                    }
                }
            },
            "Chủ đề 2. Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin": {
                "ten": "Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin",
                "noi_dung": {
                    "Bài 2: Thông tin trong môi trường số": {
                        "biet": [
                            "Nêu được các đặc điểm của thông tin trong môi trường số: đa dạng, dễ sao chép, lan truyền nhanh, khó xóa bỏ hoàn toàn.",
                            "Biết khái niệm dữ liệu số và độ tin cậy của thông tin trên mạng."
                        ],
                        "hieu": [
                            "Trình bày được các tiêu chí đánh giá độ tin cậy của nguồn thông tin (tác giả, cơ quan chủ quản, thời điểm xuất bản, mục đích).",
                            "Giải thích được sự cần thiết của việc thẩm định nguồn thông tin trước khi sử dụng."
                        ],
                        "van_dung": [
                            "Đánh giá và chọn lọc được nguồn thông tin đáng tin cậy phục vụ bài tập nghiên cứu môn học."
                        ]
                    },
                    "Bài 3: Thực hành: Khai thác thông tin số": {
                        "biet": [
                            "Biết cách sử dụng các công cụ tìm kiếm nâng cao (tìm theo định dạng file, tìm trong dấu ngoặc kép)."
                        ],
                        "hieu": [
                            "Hiểu cách trích xuất và tổng hợp thông tin từ nhiều nguồn tài liệu số khác nhau."
                        ],
                        "van_dung": [
                            "Tìm kiếm và biên tập được bản báo cáo ngắn gọn về một chủ đề học tập có chú thích nguồn rõ ràng."
                        ]
                    }
                }
            },
            "Chủ đề 3. Đạo đức, pháp luật và văn hóa trong môi trường số": {
                "ten": "Đạo đức, pháp luật và văn hóa trong môi trường số",
                "noi_dung": {
                    "Bài 4: Đạo đức và văn hóa trong sử dụng công nghệ kĩ thuật số": {
                        "biet": [
                            "Nêu được các quy định cơ bản của pháp luật về sở hữu trí tuệ và bản quyền số.",
                            "Nhận biết được hành vi đạo văn và vi phạm bản quyền phần mềm, âm nhạc, hình ảnh."
                        ],
                        "hieu": [
                            "Giải thích được hậu quả pháp lý và đạo đức của việc sử dụng sản phẩm số không có bản quyền.",
                            "Nêu được cách trích dẫn tác giả hợp lệ khi sử dụng tài liệu của người khác."
                        ],
                        "van_dung": [
                            "Tuân thủ văn hóa ứng xử số, không tải hay sử dụng phần mềm bẻ khóa (crack); luôn ghi nguồn khi làm bài thuyết trình."
                        ]
                    }
                }
            },
            "Chủ đề 4. Ứng dụng tin học": {
                "ten": "Ứng dụng tin học",
                "noi_dung": {
                    "Bài 5: Sử dụng bảng tính giải quyết bài toán thực tế": {
                        "biet": [
                            "Nhận biết được bảng tính có thể mô hình hóa và giải quyết các bài toán quản lý, tài chính thực tế.",
                            "Biết sử dụng các hàm điều kiện cơ bản."
                        ],
                        "hieu": [
                            "Hiểu cách thiết lập các mối liên hệ công thức giữa các bảng dữ liệu để tự động hóa bảng tính."
                        ],
                        "van_dung": [
                            "Xây dựng được bảng tính quản lý chi tiêu cá nhân hoặc kế hoạch kinh doanh nhỏ của học sinh."
                        ]
                    },
                    "Bài 6: Sắp xếp và lọc dữ liệu": {
                        "biet": [
                            "Biết các nút lệnh sắp xếp (Sort) theo nhiều tiêu chí và lọc (Filter) trong phần mềm bảng tính."
                        ],
                        "hieu": [
                            "Hiểu được cách lọc theo điều kiện số (Number Filters) và điều kiện văn bản (Text Filters)."
                        ],
                        "van_dung": [
                            "Lọc ra danh sách thỏa mãn đồng thời nhiều tiêu chí trong một bảng khảo sát thực tế."
                        ]
                    },
                    "Bài 7: Trình bày dữ liệu bằng biểu đồ": {
                        "biet": [
                            "Kể tên được các loại biểu đồ: biểu đồ cột (Column), biểu đồ đường (Line), biểu đồ tròn (Pie).",
                            "Biết các thành phần của biểu đồ: tiêu đề, trục tọa độ, chú giải (Legend), nhãn dữ liệu (Data Labels)."
                        ],
                        "hieu": [
                            "Lựa chọn được dạng biểu đồ thích hợp nhất tương ứng với mục đích biểu diễn số liệu."
                        ],
                        "van_dung": [
                            "Vẽ và định dạng biểu đồ hoàn chỉnh để báo cáo xu hướng phát triển từ bảng số liệu thống kê."
                        ]
                    },
                    "Bài 8a: Làm việc với danh sách dạng liệt kê và hình ảnh trong văn bản": {
                        "biet": [
                            "Biết cách tạo danh sách dấu đầu dòng (Bullets) và danh sách thứ tự (Numbering) nhiều cấp độ trong Word.",
                            "Biết cách chèn và định dạng kích thước, đường viền của hình ảnh."
                        ],
                        "hieu": [
                            "Hiểu cách thay đổi vị trí tương đối giữa hình ảnh và văn bản (Wrap Text: In Line with Text, Square, Tight...)."
                        ],
                        "van_dung": [
                            "Trình bày văn bản tờ rơi hoặc bài báo tường có danh sách phân cấp và hình ảnh chèn chuyên nghiệp."
                        ]
                    },
                    "Bài 9a: Tạo đầu trang, chân trang cho văn bản": {
                        "biet": [
                            "Nêu được khái niệm Header (Đầu trang), Footer (Chân trang) và số trang tự động.",
                            "Biết thao tác chèn Header, Footer và Page Number trong văn bản."
                        ],
                        "hieu": [
                            "Hiểu được tác dụng của việc hiển thị tiêu đề tài liệu, tên tác giả và số trang lặp lại ở mọi trang."
                        ],
                        "van_dung": [
                            "Đánh số trang và tạo đầu trang/chân trang chuẩn cho một bản báo cáo dự án học tập."
                        ]
                    },
                    "Bài 10a: Định dạng nâng cao cho trang chiếu": {
                        "biet": [
                            "Biết cách sử dụng Slide Master để tạo khuôn mẫu định dạng chung cho toàn bộ bài thuyết trình.",
                            "Biết cách áp dụng chủ đề (Themes) đồng bộ màu sắc và phông chữ."
                        ],
                        "hieu": [
                            "Giải thích được lợi ích của Slide Master giúp tiết kiệm thời gian và đảm bảo tính nhất quán của bài trình chiếu."
                        ],
                        "van_dung": [
                            "Thiết kế bài thuyết trình chuyên nghiệp sử dụng Slide Master đồng bộ logo và phông chữ trường học."
                        ]
                    },
                    "Bài 11a: Sử dụng bản mẫu tạo bài trình chiếu": {
                        "biet": [
                            "Biết cách tải và áp dụng các mẫu bản trình chiếu (Templates) có sẵn trên Internet."
                        ],
                        "hieu": [
                            "Hiểu cách tùy biến nội dung trên khung bản mẫu có sẵn."
                        ],
                        "van_dung": [
                            "Hoàn thiện bài thuyết trình báo cáo sinh hoạt chuyên đề theo mẫu thiết kế hiện đại."
                        ]
                    }
                }
            },
            "Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính": {
                "ten": "Giải quyết vấn đề với sự trợ giúp của máy tính",
                "noi_dung": {
                    "Bài 12: Từ thuật toán đến chương trình": {
                        "biet": [
                            "Nêu được mối quan hệ giữa thuật toán và chương trình máy tính.",
                            "Biết các bước chuyển từ thuật toán mô tả sang mã lệnh trong môi trường lập trình trực quan hoặc Python."
                        ],
                        "hieu": [
                            "Hiểu được cách khai báo và sử dụng biến (Variable) để lưu trữ giá trị trong chương trình.",
                            "Phân biệt được giá trị của biến và tên biến."
                        ],
                        "van_dung": [
                            "Viết được chương trình đơn giản nhập vào giá trị của biến và thực hiện phép tính số học."
                        ]
                    },
                    "Bài 13: Biểu diễn dữ liệu": {
                        "biet": [
                            "Nhận biết được các kiểu dữ liệu cơ bản: số nguyên, số thực, xâu ký tự (chuỗi), kiểu logic (True/False)."
                        ],
                        "hieu": [
                            "Giải thích được vì sao cần phân biệt các kiểu dữ liệu khi lập trình.",
                            "Hiểu các phép toán so sánh (<, <=, >, >=, ==, !=) và phép toán logic (AND, OR, NOT)."
                        ],
                        "van_dung": [
                            "Viết biểu thức logic đúng để kiểm tra một điều kiện toán học (ví dụ: số chẵn, tam giác hợp lệ)."
                        ]
                    },
                    "Bài 14: Cấu trúc điều khiển": {
                        "biet": [
                            "Biết cú pháp câu lệnh rẽ nhánh (if, if-else) và câu lệnh lặp (for, while) trong môi trường lập trình."
                        ],
                        "hieu": [
                            "Mô tả được luồng thực thi câu lệnh khi điều kiện rẽ nhánh đúng hoặc sai.",
                            "Hiểu nguyên lý hoạt động của vòng lặp đếm số lần hoặc lặp với điều kiện dừng."
                        ],
                        "van_dung": [
                            "Lập trình giải bài toán tính tổng dãy số hoặc bài toán xếp loại học lực học sinh."
                        ]
                    },
                    "Bài 15: Gỡ lỗi": {
                        "biet": [
                            "Nhận biết được hai loại lỗi phổ biến trong lập trình: Lỗi cú pháp (Syntax error) và Lỗi ngữ nghĩa/logic (Logic error)."
                        ],
                        "hieu": [
                            "Trình bày được phương pháp kiểm thử chương trình bằng các bộ dữ liệu thử (Test cases).",
                            "Biết cách đọc thông báo lỗi để xác định vị trí dòng lệnh bị sai."
                        ],
                        "van_dung": [
                            "Phát hiện và chỉnh sửa được lỗi sai trong một đoạn mã chương trình cho trước."
                        ]
                    }
                }
            },
            "Chủ đề 6. Hướng nghiệp với tin học": {
                "ten": "Hướng nghiệp với tin học",
                "noi_dung": {
                    "Bài 16: Tin học với nghề nghiệp": {
                        "biet": [
                            "Kể tên được các nhóm ngành nghề chính thuộc lĩnh vực Công nghệ thông tin (Lập trình viên, Thiết kế đồ họa, Quản trị mạng, An ninh mạng, Phân tích dữ liệu).",
                            "Biết các kỹ năng số cần thiết cho thị trường lao động hiện đại."
                        ],
                        "hieu": [
                            "Giải thích được tác động chuyển đổi của Tin học đối với các ngành nghề truyền thống (nông nghiệp thông minh, y tế số, giáo dục trực tuyến)."
                        ],
                        "van_dung": [
                            "Tự đánh giá được sở thích, năng lực cá nhân đối với các ngành nghề ứng dụng công nghệ số trong tương lai."
                        ]
                    }
                }
            }
        }
    },
    9: {
        "ten_khoi": "Tin học Lớp 9",
        "bo_sach": "Kết nối tri thức với cuộc sống",
        "ky_kiem_tra": {
            "Giữa kỳ 1": ["Bài 1: Thế giới kĩ thuật số", "Bài 2: Thông tin trong giải quyết vấn đề", "Bài 3: Thực hành: Đánh giá chất lượng thông tin", "Bài 4: Một số vấn đề pháp lí về sử dụng dịch vụ Internet"],
            "Cuối kỳ 1": ["Bài 1: Thế giới kĩ thuật số", "Bài 2: Thông tin trong giải quyết vấn đề", "Bài 3: Thực hành: Đánh giá chất lượng thông tin", "Bài 4: Một số vấn đề pháp lí về sử dụng dịch vụ Internet", "Bài 5: Tìm hiểu phần mềm mô phỏng", "Bài 6: Thực hành: Khai thác phần mềm mô phỏng", "Bài 7: Trình bày thông tin trong trao đổi và hợp tác", "Bài 8: Thực hành: Sử dụng công cụ trực quan trình bày thông tin trong trao đổi và hợp tác"],
            "Giữa kỳ 2": ["Bài 9a: Sử dụng công cụ xác thực dữ liệu", "Bài 10a: Sử dụng hàm COUNTIF", "Bài 11a: Sử dụng hàm SUMIF", "Bài 12a: Sử dụng hàm IF", "Bài 13a: Hoàn thiện bảng tính quản lí tài chính gia đình"],
            "Cuối kỳ 2": ["Bài 10a: Sử dụng hàm COUNTIF", "Bài 11a: Sử dụng hàm SUMIF", "Bài 12a: Sử dụng hàm IF", "Bài 14: Giải quyết vấn đề", "Bài 15: Bài toán tin học", "Bài 16: Thực hành: Lập chương trình máy tính", "Bài 17: Tin học và thế giới nghề nghiệp"]
        },
        "chu_de": {
            "Chủ đề 1. Máy tính và cộng đồng": {
                "ten": "Máy tính và cộng đồng",
                "noi_dung": {
                    "Bài 1: Thế giới kĩ thuật số": {
                        "biet": [
                            "Nhận biết được các thiết bị số thông minh xung quanh đời sống: điện thoại thông minh, đồng hồ thông minh, TV thông minh, nhà thông minh (Smart Home).",
                            "Biết khái niệm Internet of Things (IoT) - Vạn vật kết nối Internet."
                        ],
                        "hieu": [
                            "Giải thích được sự thay đổi tích cực và những thách thức của thế giới kỹ thuật số đối với đời sống con người."
                        ],
                        "van_dung": [
                            "Đề xuất được ý tưởng ứng dụng thiết bị số thông minh để nâng cao chất lượng cuộc sống hoặc học tập."
                        ]
                    }
                }
            },
            "Chủ đề 2. Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin": {
                "ten": "Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin",
                "noi_dung": {
                    "Bài 2: Thông tin trong giải quyết vấn đề": {
                        "biet": [
                            "Nêu được vai trò quyết định của chất lượng thông tin trong việc giải quyết vấn đề.",
                            "Biết các tiêu chí đo lường chất lượng thông tin: tính chính xác, tính đầy đủ, tính cập nhật, tính liên quan."
                        ],
                        "hieu": [
                            "Giải thích được hậu quả khi đưa ra quyết định dựa trên thông tin thiếu chính xác hoặc lỗi thời."
                        ],
                        "van_dung": [
                            "Thu thập và sàng lọc được các nguồn thông tin có độ tin cậy cao để giải quyết một nhiệm vụ học tập."
                        ]
                    },
                    "Bài 3: Thực hành: Đánh giá chất lượng thông tin": {
                        "biet": [
                            "Biết các bước kiểm tra nguồn gốc, tác giả và ngày đăng tải của bài viết trên Internet."
                        ],
                        "hieu": [
                            "Phân tích được tính khách quan và phát hiện các dấu hiệu thiên vị, quảng cáo trá hình trong bài viết."
                        ],
                        "van_dung": [
                            "Thẩm định và đánh giá được độ xác thực của thông tin từ 2 trang web khác nhau về cùng một sự kiện."
                        ]
                    }
                }
            },
            "Chủ đề 3. Đạo đức, pháp luật và văn hóa trong môi trường số": {
                "ten": "Đạo đức, pháp luật và văn hóa trong môi trường số",
                "noi_dung": {
                    "Bài 4: Một số vấn đề pháp lí về sử dụng dịch vụ Internet": {
                        "biet": [
                            "Nêu được các điều khoản cơ bản trong Luật An ninh mạng Việt Nam liên quan đến hành vi của cá nhân.",
                            "Nhận biết các hành vi vi phạm pháp luật trên mạng: xúc phạm danh dự, phát tán văn hóa phẩm độc hại, tấn công mạng."
                        ],
                        "hieu": [
                            "Giải thích được trách nhiệm pháp lý và hình thức xử phạt khi vi phạm quy định sử dụng dịch vụ Internet.",
                            "Hiểu được quyền được bảo vệ danh dự, nhân phẩm và quyền riêng tư trên không gian số."
                        ],
                        "van_dung": [
                            "Thể hiện thái độ phê phán đối với các hành vi sai trái trên mạng và tuyên truyền an toàn thông tin cho bạn bè."
                        ]
                    }
                }
            },
            "Chủ đề 4. Ứng dụng tin học": {
                "ten": "Ứng dụng tin học",
                "noi_dung": {
                    "Bài 5: Tìm hiểu phần mềm mô phỏng": {
                        "biet": [
                            "Nêu được khái niệm phần mềm mô phỏng và kể tên một số phần mềm mô phỏng trong học tập (mô phỏng Vật lý, Hóa học, Sinh học, Toán học).",
                            "Biết lợi ích của phần mềm mô phỏng trong việc trực quan hóa các hiện tượng khó quan sát ngoài thực tế."
                        ],
                        "hieu": [
                            "Giải thích được sự khác nhau giữa thí nghiệm thực tế và thí nghiệm mô phỏng trên máy tính."
                        ],
                        "van_dung": [
                            "Khai thác phần mềm mô phỏng để tự học và tìm hiểu một định luật khoa học tự nhiên."
                        ]
                    },
                    "Bài 6: Thực hành: Khai thác phần mềm mô phỏng": {
                        "biet": [
                            "Biết các nút điều khiển, tham số đầu vào trong phần mềm mô phỏng."
                        ],
                        "hieu": [
                            "Hiểu cách thay đổi tham số để quan sát sự biến đổi của đối tượng mô phỏng."
                        ],
                        "van_dung": [
                            "Thực hiện thí nghiệm mô phỏng và ghi lại kết quả đo lường thành bảng số liệu khoa học."
                        ]
                    },
                    "Bài 7: Trình bày thông tin trong trao đổi và hợp tác": {
                        "biet": [
                            "Kể tên các công cụ số hỗ trợ làm việc nhóm trực tuyến: Google Docs, Microsoft Teams, Trello, Google Drive."
                        ],
                        "hieu": [
                            "Hiểu được cách chia sẻ tài liệu và phân quyền truy cập (chỉ xem, nhận xét, chỉnh sửa)."
                        ],
                        "van_dung": [
                            "Tham gia làm việc nhóm trực tuyến để cùng soạn thảo một văn bản hoặc bài thuyết trình."
                        ]
                    },
                    "Bài 8: Thực hành: Sử dụng công cụ trực quan trình bày thông tin trong trao đổi và hợp tác": {
                        "biet": [
                            "Biết cách theo dõi lịch sử chỉnh sửa và nhận xét (Comment) trong tài liệu dùng chung."
                        ],
                        "hieu": [
                            "Hiểu quy tắc phối hợp lịch sự, tránh ghi đè dữ liệu của người khác khi làm việc chung."
                        ],
                        "van_dung": [
                            "Phối hợp hoàn thành bài tập nhóm trực tuyến hiệu quả và đúng thời hạn."
                        ]
                    },
                    "Bài 9a: Sử dụng công cụ xác thực dữ liệu": {
                        "biet": [
                            "Biết tính năng Data Validation (Xác thực dữ liệu) trong phần mềm bảng tính.",
                            "Kể tên các kiểu giới hạn nhập liệu: số nguyên trong khoảng, danh sách lựa chọn (List), độ dài văn bản."
                        ],
                        "hieu": [
                            "Giải thích được tác dụng của việc xác thực dữ liệu giúp hạn chế tối đa sai sót khi người dùng nhập liệu."
                        ],
                        "van_dung": [
                            "Thiết lập bảng nhập điểm có giới hạn số từ 0 đến 10 và tạo danh sách chọn giới tính (Nam/Nữ) tự động."
                        ]
                    },
                    "Bài 10a: Sử dụng hàm COUNTIF": {
                        "biet": [
                            "Nêu được công dụng của hàm COUNTIF: đếm số ô thỏa mãn một điều kiện cho trước.",
                            "Biết cú pháp: COUNTIF(range, criteria)."
                        ],
                        "hieu": [
                            "Hiểu cách đặt biểu thức điều kiện (số, ký tự, chuỗi so sánh như \">=8\") trong hàm COUNTIF."
                        ],
                        "van_dung": [
                            "Sử dụng hàm COUNTIF để đếm số học sinh đạt điểm Giỏi hoặc đếm số học sinh nữ trong lớp."
                        ]
                    },
                    "Bài 11a: Sử dụng hàm SUMIF": {
                        "biet": [
                            "Nêu được công dụng của hàm SUMIF: tính tổng các ô thỏa mãn một điều kiện xác định.",
                            "Biết cú pháp: SUMIF(range, criteria, [sum_range])."
                        ],
                        "hieu": [
                            "Phân biệt được vùng kiểm tra điều kiện (range) và vùng thực hiện tính tổng (sum_range)."
                        ],
                        "van_dung": [
                            "Tính tổng học bổng hoặc tổng tiền quỹ chi cho một hoạt động cụ thể theo điều kiện."
                        ]
                    },
                    "Bài 12a: Sử dụng hàm IF": {
                        "biet": [
                            "Nêu được công dụng của hàm điều kiện logic IF.",
                            "Biết cú pháp: IF(logical_test, value_if_true, value_if_false)."
                        ],
                        "hieu": [
                            "Hiểu nguyên lý trả về kết quả tương ứng khi điều kiện kiểm tra nhận giá trị True hoặc False.",
                            "Biết cách lồng ghép các hàm IF để xử lý nhiều mức xếp loại."
                        ],
                        "van_dung": [
                            "Sử dụng hàm IF để tự động xét điều kiện Đạt/Chưa đạt hoặc xếp loại học lực học sinh."
                        ]
                    },
                    "Bài 13a: Hoàn thiện bảng tính quản lí tài chính gia đình": {
                        "biet": [
                            "Biết cấu trúc của một bảng tính quản lý thu chi tài chính gia đình."
                        ],
                        "hieu": [
                            "Hiểu cách liên kết các hàm SUM, SUMIF, COUNTIF, IF để tổng hợp số liệu thu chi theo tháng."
                        ],
                        "van_dung": [
                            "Xây dựng hoàn chỉnh bảng tính dự toán thu chi cá nhân hoặc gia đình có biểu đồ phân tích trực quan."
                        ]
                    }
                }
            },
            "Chủ đề 5. Giải quyết vấn đề với sự trợ giúp của máy tính": {
                "ten": "Giải quyết vấn đề với sự trợ giúp của máy tính",
                "noi_dung": {
                    "Bài 14: Giải quyết vấn đề": {
                        "biet": [
                            "Nêu được các bước trong quy trình giải quyết vấn đề: Xác định bài toán, Lập kế hoạch, Thực hiện, Đánh giá kết quả."
                        ],
                        "hieu": [
                            "Hiểu được cách chia một bài toán lớn phức tạp thành các bài toán con nhỏ hơn để giải quyết tuần tự."
                        ],
                        "van_dung": [
                            "Phân rã một tình huống thực tế thành các bước cụ thể để lập trình trên máy tính."
                        ]
                    },
                    "Bài 15: Bài toán tin học": {
                        "biet": [
                            "Xác định được Input (Dữ liệu vào) và Output (Kết quả ra) của một bài toán tin học."
                        ],
                        "hieu": [
                            "Trình bày được mối quan hệ giữa Input và Output thông qua giải thuật xử lý."
                        ],
                        "van_dung": [
                            "Mô tả chính xác Input và Output của bài toán quản lý thư viện trường học hoặc bài toán tính cước taxi."
                        ]
                    },
                    "Bài 16: Thực hành: Lập chương trình máy tính": {
                        "biet": [
                            "Biết cách viết mã lệnh hoàn chỉnh để cài đặt thuật toán bằng ngôn ngữ lập trình."
                        ],
                        "hieu": [
                            "Hiểu cách phối hợp biến, mảng dữ liệu (danh sách), cấu trúc rẽ nhánh và vòng lặp trong chương trình."
                        ],
                        "van_dung": [
                            "Lập trình và chạy thử thành công một chương trình tính toán số học hoặc trò chơi tương tác nhỏ."
                        ]
                    }
                }
            },
            "Chủ đề 6. Hướng nghiệp với tin học": {
                "ten": "Hướng nghiệp với tin học",
                "noi_dung": {
                    "Bài 17: Tin học và thế giới nghề nghiệp": {
                        "biet": [
                            "Kể tên được các ngành nghề trong xã hội hiện đại có ứng dụng sâu rộng của Tin học và AI.",
                            "Biết vai trò của việc học tập suốt đời và nâng cao kỹ năng số."
                        ],
                        "hieu": [
                            "Giải thích được các kỹ năng mềm bổ trợ quan trọng: tư duy logic, giải quyết vấn đề, hợp tác nhóm, đạo đức số."
                        ],
                        "van_dung": [
                            "Lập kế hoạch rèn luyện kỹ năng tin học cá nhân định hướng nghề nghiệp tương lai."
                        ]
                    }
                }
            }
        }
    }
}

# Convert string keys to int keys in code
import pprint

content = '''"""
Dữ liệu chuẩn hóa Chương trình Giáo dục Phổ thông 2018 môn Tin học cấp THCS (Lớp 6, 7, 8, 9).
Bộ sách giáo khoa: KẾT NỐI TRI THỨC VỚI CUỘC SỐNG (NXB Giáo dục Việt Nam).
Được số hóa chi tiết đến từng BÀI HỌC và YÊU CẦU CẦN ĐẠT (YCCĐ) theo 3 mức độ nhận thức:
- Biết (Nhận biết)
- Hiểu (Thông hiểu)
- Vận dụng (Vận dụng & Vận dụng cao)
"""

CURRICULUM_DATA = ''' + pprint.pformat(kntt_data, indent=4, width=120) + "\n"

# Add string keys as aliases so CURRICULUM_DATA[6] and CURRICULUM_DATA['6'] both work
content += '''
for _k in list(CURRICULUM_DATA.keys()):
    if isinstance(_k, int):
        CURRICULUM_DATA[str(_k)] = CURRICULUM_DATA[_k]
'''

with open("curriculum_data.py", "w", encoding="utf-8") as f:
    f.write(content)

print("curriculum_data.py updated successfully with 100% KNTT lessons!")

