"""
Dữ liệu chuẩn hóa Chương trình Giáo dục Phổ thông 2018 môn Tin học cấp THCS (Lớp 6, 7, 8, 9).
Bao gồm: Các Chủ đề (A -> F), Bài học, Nội dung đơn vị kiến thức và Yêu cầu cần đạt (YCCĐ)
được phân rã theo 3 mức độ nhận thức: Biết (Nhận biết), Hiểu (Thông hiểu), Vận dụng (Vận dụng & Vận dụng cao).
"""

CURRICULUM_DATA = {
    6: {
        "ten_khoi": "Tin học Lớp 6",
        "ky_kiem_tra": {
            "Giữa kỳ 1": ["Chủ đề A", "Chủ đề B"],
            "Cuối kỳ 1": ["Chủ đề A", "Chủ đề B", "Chủ đề C"],
            "Giữa kỳ 2": ["Chủ đề D", "Chủ đề E"],
            "Cuối kỳ 2": ["Chủ đề D", "Chủ đề E", "Chủ đề F"]
        },
        "chu_de": {
            "Chủ đề A": {
                "ten": "Máy tính và cộng đồng",
                "noi_dung": {
                    "Thông tin và dữ liệu": {
                        "biet": [
                            "Nêu được ví dụ về thông tin và dữ liệu thu nhận được từ các giác quan của con người.",
                            "Nhận biết được tầm quan trọng của thông tin trong đời sống hàng ngày."
                        ],
                        "hieu": [
                            "Giải thích được sự khác nhau giữa thông tin và vật mang tin.",
                            "Nêu được ví dụ về vai trò của thông tin trong việc ra quyết định."
                        ],
                        "van_dung": [
                            "Phân tích được một tình huống thực tế để chỉ ra đâu là thông tin, đâu là dữ liệu và vật mang tin.",
                            "Vận dụng kiến thức để thu thập đúng thông tin cần thiết phục vụ học tập."
                        ]
                    },
                    "Lưu trữ và trao đổi thông tin": {
                        "biet": [
                            "Nêu được các thao tác cơ bản trong quá trình xử lý thông tin của máy tính (thu nhận, lưu trữ, xử lý, truyền tải).",
                            "Biết các đơn vị đo dung lượng thông tin cơ bản: Bit, Byte, KB, MB, GB, TB."
                        ],
                        "hieu": [
                            "Giải thích được máy tính xử lý dữ liệu ở dạng nhị phân (0 và 1).",
                            "Quy đổi được giữa các đơn vị đo dung lượng thông tin thông dụng."
                        ],
                        "van_dung": [
                            "Tính toán được dung lượng thẻ nhớ, USB cần thiết để lưu trữ một số lượng tài liệu, bài giảng cụ thể."
                        ]
                    },
                    "Mạng máy tính và Internet": {
                        "biet": [
                            "Nêu được khái niệm mạng máy tính và các thành phần chính của mạng.",
                            "Kể tên được một số thiết bị kết nối mạng thông dụng: modem, router, switch, cáp mạng."
                        ],
                        "hieu": [
                            "Giải thích được lợi ích của mạng máy tính trong chia sẻ dữ liệu và thiết bị phần cứng.",
                            "Phân biệt được mạng có dây và mạng không dây."
                        ],
                        "van_dung": [
                            "Mô tả được cách kết nối các thiết bị trong gia đình hoặc phòng học vào mạng không dây (Wi-Fi)."
                        ]
                    }
                }
            },
            "Chủ đề B": {
                "ten": "Mạng máy tính và Internet",
                "noi_dung": {
                    "Thông tin trên Internet": {
                        "biet": [
                            "Nêu được khái niệm World Wide Web (WWW), website, địa chỉ trang web, trình duyệt web.",
                            "Kể tên được một số trình duyệt web phổ biến hiện nay (Chrome, Edge, Firefox, Cốc Cốc)."
                        ],
                        "hieu": [
                            "Trình bày được cách thức sử dụng máy tìm kiếm để tra cứu thông tin bằng từ khóa.",
                            "Giải thích được tác dụng của việc sử dụng từ khóa chính xác khi tìm kiếm."
                        ],
                        "van_dung": [
                            "Tìm kiếm được thông tin phục vụ một bài học cụ thể bằng cách kết hợp các từ khóa hiệu quả."
                        ]
                    },
                    "Thư điện tử (Email)": {
                        "biet": [
                            "Nêu được khái niệm thư điện tử và địa chỉ thư điện tử.",
                            "Nhận biết được cấu trúc của một địa chỉ email chuẩn (tên_người_dùng@tên_miền)."
                        ],
                        "hieu": [
                            "Giải thích được ưu điểm và nhược điểm của thư điện tử so với thư truyền thống.",
                            "Phân biệt được các trường Đến (To), Đồng gửi (Cc), Bản sao ẩn (Bcc) và Tệp đính kèm (Attachment)."
                        ],
                        "van_dung": [
                            "Soạn và gửi được một bức thư điện tử có tệp đính kèm gửi thầy cô giáo hoặc bạn bè."
                        ]
                    }
                }
            },
            "Chủ đề C": {
                "ten": "Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin",
                "noi_dung": {
                    "Sắp xếp và quản lý tệp tin": {
                        "biet": [
                            "Biết được cấu trúc phân cấp cây thư mục trong hệ điều hành máy tính.",
                            "Nhận biết được tên tệp gồm phần tên và phần mở rộng (đuôi tệp)."
                        ],
                        "hieu": [
                            "Giải thích được sự cần thiết của việc tổ chức lưu trữ tệp và thư mục một cách khoa học.",
                            "Phân biệt được các dạng tệp tin thông dụng qua phần mở rộng (.docx, .xlsx, .pptx, .pdf, .mp3, .mp4)."
                        ],
                        "van_dung": [
                            "Tạo lập được cây thư mục khoa học trên máy tính cá nhân để quản lý bài học các môn."
                        ]
                    }
                }
            },
            "Chủ đề D": {
                "ten": "Đạo đức, pháp luật và văn hóa trong môi trường số",
                "noi_dung": {
                    "Bản quyền và an toàn thông tin": {
                        "biet": [
                            "Nêu được khái niệm bản quyền nội dung số và phần mềm.",
                            "Nhận biết được những tác hại của việc lộ mật khẩu hoặc thông tin cá nhân trên mạng."
                        ],
                        "hieu": [
                            "Giải thích được lý do cần tôn trọng bản quyền và sử dụng phần mềm có bản quyền.",
                            "Trình bày được quy tắc ứng xử văn minh, lịch sự khi giao tiếp trên mạng xã hội."
                        ],
                        "van_dung": [
                            "Thực hiện đặt mật khẩu mạnh và không chia sẻ tài khoản cá nhân cho người lạ.",
                            "Biết trích dẫn nguồn tác giả khi sử dụng tài liệu, hình ảnh từ Internet trong bài tập."
                        ]
                    }
                }
            },
            "Chủ đề E": {
                "ten": "Ứng dụng tin học",
                "noi_dung": {
                    "Soạn thảo văn bản cơ bản": {
                        "biet": [
                            "Nhận biết các thành phần cơ bản của văn bản: ký tự, từ, câu, đoạn văn bản, trang.",
                            "Biết các thao tác định dạng văn bản: phông chữ, cỡ chữ, kiểu chữ, màu chữ, căn lề."
                        ],
                        "hieu": [
                            "Hiểu được quy tắc gõ tiếng Việt có dấu theo kiểu Telex hoặc Vni.",
                            "Phân biệt được định dạng ký tự và định dạng đoạn văn bản."
                        ],
                        "van_dung": [
                            "Soạn thảo và trình bày được một văn bản hoàn chỉnh có tiêu đề, nội dung và chèn hình ảnh minh họa."
                        ]
                    },
                    "Sơ đồ tư duy": {
                        "biet": [
                            "Nêu được khái niệm và công dụng của sơ đồ tư duy trong học tập.",
                            "Nhận biết các thành phần của sơ đồ tư duy: chủ đề chính, nhánh chính, nhánh phụ, từ khóa."
                        ],
                        "hieu": [
                            "Trình bày được các bước tóm tắt nội dung một bài học dưới dạng sơ đồ tư duy."
                        ],
                        "van_dung": [
                            "Vẽ được một sơ đồ tư duy bằng tay hoặc bằng phần mềm để ôn tập một bài học cụ thể."
                        ]
                    }
                }
            },
            "Chủ đề F": {
                "ten": "Giải quyết vấn đề với sự trợ giúp của máy tính",
                "noi_dung": {
                    "Thuật toán và mô tả thuật toán": {
                        "biet": [
                            "Nêu được khái niệm thuật toán.",
                            "Biết hai cách mô tả thuật toán: liệt kê các bước bằng ngôn ngữ tự nhiên và sơ đồ khối."
                        ],
                        "hieu": [
                            "Giải thích được ý nghĩa các hình khối chuẩn trong sơ đồ khối (hình elip, hình chữ nhật, hình thoi, hình bình hành, mũi tên).",
                            "Hiểu được 3 cấu trúc điều khiển cơ bản: tuần tự, rẽ nhánh và lặp."
                        ],
                        "van_dung": [
                            "Vẽ được sơ đồ khối hoặc liệt kê các bước mô tả thuật toán giải một bài toán thực tế đơn giản (ví dụ: pha trà, giải bài toán tìm số lớn nhất)."
                        ]
                    }
                }
            }
        }
    },
    7: {
        "ten_khoi": "Tin học Lớp 7",
        "ky_kiem_tra": {
            "Giữa kỳ 1": ["Chủ đề A", "Chủ đề B"],
            "Cuối kỳ 1": ["Chủ đề A", "Chủ đề B", "Chủ đề E (Bảng tính 1)"],
            "Giữa kỳ 2": ["Chủ đề D", "Chủ đề E (Bảng tính 2)"],
            "Cuối kỳ 2": ["Chủ đề D", "Chủ đề E (Bảng tính 2)", "Chủ đề F"]
        },
        "chu_de": {
            "Chủ đề A": {
                "ten": "Máy tính và cộng đồng",
                "noi_dung": {
                    "Thiết bị vào - ra và hệ điều hành": {
                        "biet": [
                            "Kể tên và phân loại được các thiết bị vào (chuột, bàn phím, micro, máy quét) và thiết bị ra (màn hình, máy in, loa, máy chiếu).",
                            "Nêu được chức năng cơ bản của hệ điều hành và phần mềm ứng dụng."
                        ],
                        "hieu": [
                            "Phân biệt được sự khác nhau giữa hệ điều hành (Windows, Linux, macOS, Android, iOS) và phần mềm ứng dụng (Word, Excel, trình duyệt).",
                            "Giải thích được mối quan hệ phối hợp giữa phần cứng, hệ điều hành và phần mềm ứng dụng."
                        ],
                        "van_dung": [
                            "Thao tác an toàn khi gắn và tháo thiết bị lưu trữ ngoài (USB) trên máy tính."
                        ]
                    }
                }
            },
            "Chủ đề B": {
                "ten": "Mạng máy tính và Internet",
                "noi_dung": {
                    "Mạng xã hội và giao tiếp trực tuyến": {
                        "biet": [
                            "Nêu được một số kênh trao đổi thông tin thông dụng trên Internet: email, diễn đàn, mạng xã hội, ứng dụng nhắn tin tức thời.",
                            "Kể tên được một số mạng xã hội phổ biến."
                        ],
                        "hieu": [
                            "Trình bày được các chức năng cơ bản của mạng xã hội: tạo trang cá nhân, kết bạn, chia sẻ bài viết, tương tác (like, comment, share).",
                            "Nêu được mặt trái và những nguy cơ tiềm ẩn khi tham gia mạng xã hội."
                        ],
                        "van_dung": [
                            "Ứng xử chuẩn mực, lịch sự khi bình luận, chia sẻ thông tin trên mạng xã hội."
                        ]
                    }
                }
            },
            "Chủ đề D": {
                "ten": "Đạo đức, pháp luật và văn hóa trong môi trường số",
                "noi_dung": {
                    "Ứng xử văn hóa và an toàn trên mạng": {
                        "biet": [
                            "Nêu được các quy định cơ bản về bảo vệ thông tin cá nhân và quyền riêng tư trên không gian mạng.",
                            "Nhận biết được các dấu hiệu của lừa đảo trực tuyến và bạo lực mạng."
                        ],
                        "hieu": [
                            "Giải thích được tác hại của việc lan truyền thông tin sai sự thật (fake news).",
                            "Biết cách phòng tránh và xử lý khi gặp tình huống bị quấy rối hoặc bạo lực trên mạng."
                        ],
                        "van_dung": [
                            "Kiểm chứng thông tin trước khi chia sẻ; bảo mật tài khoản mạng xã hội bằng xác thực hai yếu tố."
                        ]
                    }
                }
            },
            "Chủ đề E (Bảng tính 1)": {
                "ten": "Ứng dụng tin học - Làm quen phần mềm bảng tính",
                "noi_dung": {
                    "Bảng tính điện tử cơ bản": {
                        "biet": [
                            "Nhận biết được giao diện của phần mềm bảng tính (Excel): thanh bảng chọn, thanh công thức, ô, hàng, cột, trang tính.",
                            "Nhận biết địa chỉ ô, khối ô và các kiểu dữ liệu cơ bản: số, văn bản, ngày tháng."
                        ],
                        "hieu": [
                            "Hiểu cách nhập và chỉnh sửa dữ liệu trong bảng tính.",
                            "Phân biệt được cách căn lề mặc định của dữ liệu số (bên phải) và văn bản (bên trái)."
                        ],
                        "van_dung": [
                            "Tạo lập được bảng tính danh sách lớp hoặc bảng điểm đơn giản."
                        ]
                    }
                }
            },
            "Chủ đề E (Bảng tính 2)": {
                "ten": "Ứng dụng tin học - Tính toán và trực quan hóa dữ liệu",
                "noi_dung": {
                    "Công thức và hàm tính toán": {
                        "biet": [
                            "Biết cú pháp sử dụng công thức bắt đầu bằng dấu '='.",
                            "Kể tên và nêu công dụng của các hàm cơ bản: SUM (tính tổng), AVERAGE (trung bình), COUNT (đếm số), MAX (giá trị lớn nhất), MIN (giá trị nhỏ nhất)."
                        ],
                        "hieu": [
                            "Giải thích được ý nghĩa của địa chỉ tương đối khi sao chép công thức sang ô khác.",
                            "Hiểu được cách chọn vùng dữ liệu phù hợp để áp dụng hàm tính toán."
                        ],
                        "van_dung": [
                            "Vận dụng các hàm SUM, AVERAGE, MAX, MIN để tính toán bảng tổng kết điểm học tập hoặc chi tiêu của lớp."
                        ]
                    },
                    "Trình bày và biểu đồ bảng tính": {
                        "biet": [
                            "Biết các thao tác định dạng bảng tính: kẻ viền, tô màu nền, gộp ô, định dạng số thập phân, phần trăm.",
                            "Biết các loại biểu đồ thông dụng: biểu đồ cột, biểu đồ đường, biểu đồ tròn."
                        ],
                        "hieu": [
                            "Giải thích được khi nào nên sử dụng biểu đồ cột (so sánh số liệu), biểu đồ tròn (tỷ lệ thành phần), biểu đồ đường (xu hướng theo thời gian)."
                        ],
                        "van_dung": [
                            "Vẽ được biểu đồ thích hợp để minh họa số liệu của bảng tính và rút ra nhận xét."
                        ]
                    }
                }
            },
            "Chủ đề F": {
                "ten": "Giải quyết vấn đề với sự trợ giúp của máy tính",
                "noi_dung": {
                    "Thuật toán tìm kiếm và sắp xếp": {
                        "biet": [
                            "Nêu được bài toán tìm kiếm và bài toán sắp xếp trong thực tế.",
                            "Biết tên các thuật toán: Tìm kiếm tuần tự (Linear Search), Tìm kiếm nhị phân (Binary Search), Sắp xếp nổi bọt (Bubble Sort), Sắp xếp chọn (Selection Sort)."
                        ],
                        "hieu": [
                            "Mô tả được các bước thực hiện thuật toán tìm kiếm tuần tự và nhị phân trên một danh sách cụ thể.",
                            "Giải thích được điều kiện để áp dụng tìm kiếm nhị phân (danh sách đã được sắp xếp)."
                        ],
                        "van_dung": [
                            "Mô phỏng từng bước thực hiện thuật toán sắp xếp nổi bọt hoặc sắp xếp chọn để sắp xếp một dãy số từ nhỏ đến lớn."
                        ]
                    }
                }
            }
        }
    },
    8: {
        "ten_khoi": "Tin học Lớp 8",
        "ky_kiem_tra": {
            "Giữa kỳ 1": ["Chủ đề A", "Chủ đề B"],
            "Cuối kỳ 1": ["Chủ đề A", "Chủ đề B", "Chủ đề E (Xử lý đồ họa)"],
            "Giữa kỳ 2": ["Chủ đề D", "Chủ đề F (Lập trình 1)"],
            "Cuối kỳ 2": ["Chủ đề D", "Chủ đề F (Lập trình 1)", "Chủ đề F (Lập trình 2)"]
        },
        "chu_de": {
            "Chủ đề A": {
                "ten": "Máy tính và cộng đồng",
                "noi_dung": {
                    "Lịch sử phát triển máy tính": {
                        "biet": [
                            "Nêu được các mốc chính trong lịch sử phát triển máy tính (5 thế hệ máy tính).",
                            "Nhận biết được xu hướng phát triển của thiết bị số: thu nhỏ kích thước, tăng tốc độ xử lý, tiết kiệm năng lượng, kết nối thông minh."
                        ],
                        "hieu": [
                            "Giải thích được sự đóng góp của máy tính vào sự thay đổi của các ngành nghề trong xã hội."
                        ],
                        "van_dung": [
                            "Nhận diện được các thiết bị thông minh hiện diện trong đời sống hàng ngày (smart phone, smart watch, robot hút bụi...)."
                        ]
                    }
                }
            },
            "Chủ đề B": {
                "ten": "Mạng máy tính và Internet",
                "noi_dung": {
                    "Thông tin đáng tin cậy và tìm kiếm nâng cao": {
                        "biet": [
                            "Biết các tiêu chí đánh giá độ tin cậy của thông tin trên Internet: tác giả, cơ quan chủ quản, thời điểm xuất bản, mục đích thông tin.",
                            "Biết các toán tử tìm kiếm nâng cao (+, -, AND, OR, dấu ngoặc kép \"\")."
                        ],
                        "hieu": [
                            "Phân tích được lý do vì sao không phải mọi thông tin trên Internet đều chính xác.",
                            "Hiểu được cơ chế hoạt động của toán tử tìm kiếm để thu hẹp kết quả tìm kiếm."
                        ],
                        "van_dung": [
                            "Sử dụng toán tử tìm kiếm nâng cao để tra cứu tài liệu học tập chính thống và loại bỏ kết quả rác."
                        ]
                    }
                }
            },
            "Chủ đề D": {
                "ten": "Đạo đức, pháp luật và văn hóa trong môi trường số",
                "noi_dung": {
                    "Đạo đức và pháp luật công nghệ thông tin": {
                        "biet": [
                            "Nêu được một số điều khoản cơ bản của Luật An ninh mạng Việt Nam liên quan đến hành vi người dùng học sinh.",
                            "Nhận biết được phần mềm độc hại (Virus, Worm, Trojan, Ransomware) và tác hại của chúng."
                        ],
                        "hieu": [
                            "Giải thích được trách nhiệm pháp lý khi chia sẻ hoặc phát tán thông tin xuyên tạc, xúc phạm người khác.",
                            "Nêu được các biện pháp phòng chống phần mềm độc hại (cài antivirus, quét mã, không mở file lạ)."
                        ],
                        "van_dung": [
                            "Thực hành quét virus và kiểm tra tính an toàn của liên kết (link) trước khi bấm."
                        ]
                    }
                }
            },
            "Chủ đề E (Xử lý đồ họa)": {
                "ten": "Ứng dụng tin học - Xử lý ảnh và đồ họa số",
                "noi_dung": {
                    "Phần mềm chỉnh sửa ảnh": {
                        "biet": [
                            "Nhận biết được khái niệm ảnh raster (ảnh bitmap) và ảnh vector.",
                            "Biết các công cụ cơ bản của phần mềm chỉnh sửa ảnh (cắt, xoay, chỉnh màu, lớp - layers)."
                        ],
                        "hieu": [
                            "Giải thích được nguyên tắc hoạt động của các lớp ảnh (layers).",
                            "Hiểu cách xuất ảnh theo các định dạng phổ biến (.jpg, .png) phù hợp mục đích sử dụng."
                        ],
                        "van_dung": [
                            "Thiết kế được một áp phích (poster) hoặc chỉnh sửa ảnh hoạt động của lớp để đăng báo tường."
                        ]
                    }
                }
            },
            "Chủ đề F (Lập trình 1)": {
                "ten": "Giải quyết vấn đề với sự trợ giúp của máy tính - Làm quen Lập trình",
                "noi_dung": {
                    "Biến, kiểu dữ liệu và biểu thức": {
                        "biet": [
                            "Nêu được khái niệm biến, hằng trong lập trình.",
                            "Nhận biết các kiểu dữ liệu cơ bản: số nguyên (int), số thực (float), chuỗi ký tự (str), logic (bool)."
                        ],
                        "hieu": [
                            "Hiểu quy tắc đặt tên biến hợp lệ và cách gán giá trị cho biến.",
                            "Tính toán được giá trị của các biểu thức số học và biểu thức quan hệ logic."
                        ],
                        "van_dung": [
                            "Viết được chương trình đơn giản nhập vào hai số và tính tổng, hiệu, tích, thương."
                        ]
                    }
                }
            },
            "Chủ đề F (Lập trình 2)": {
                "ten": "Giải quyết vấn đề với sự trợ giúp của máy tính - Cấu trúc điều khiển",
                "noi_dung": {
                    "Cấu trúc rẽ nhánh và lặp": {
                        "biet": [
                            "Cú pháp câu lệnh điều kiện if, if-else.",
                            "Cú pháp câu lệnh lặp for, while."
                        ],
                        "hieu": [
                            "Giải thích được luồng thực thi của câu lệnh điều kiện và câu lệnh lặp.",
                            "Phân biệt được vòng lặp với số lần biết trước (for) và lặp với số lần chưa biết trước (while)."
                        ],
                        "van_dung": [
                            "Viết chương trình kiểm tra một số là chẵn hay lẻ, tìm số lớn nhất trong ba số.",
                            "Viết chương trình tính tổng dãy số từ 1 đến N bằng vòng lặp."
                        ]
                    }
                }
            }
        }
    },
    9: {
        "ten_khoi": "Tin học Lớp 9",
        "ky_kiem_tra": {
            "Giữa kỳ 1": ["Chủ đề A", "Chủ đề B"],
            "Cuối kỳ 1": ["Chủ đề A", "Chủ đề B", "Chủ đề C & D"],
            "Giữa kỳ 2": ["Chủ đề E"],
            "Cuối kỳ 2": ["Chủ đề E", "Chủ đề F"]
        },
        "chu_de": {
            "Chủ đề A": {
                "ten": "Máy tính và cộng đồng",
                "noi_dung": {
                    "Điện toán đám mây và Dịch vụ số": {
                        "biet": [
                            "Nêu được khái niệm điện toán đám mây (Cloud Computing) và các dịch vụ lưu trữ đám mây phổ biến (Google Drive, OneDrive, iCloud).",
                            "Biết lợi ích của việc lưu trữ và làm việc cộng tác trực tuyến trên đám mây."
                        ],
                        "hieu": [
                            "Giải thích được cơ chế đồng bộ hóa dữ liệu giữa thiết bị cá nhân và đám mây.",
                            "So sánh được ưu điểm và hạn chế của lưu trữ cục bộ so với lưu trữ đám mây."
                        ],
                        "van_dung": [
                            "Thực hiện lưu trữ, phân quyền chia sẻ tệp (xem, nhận xét, chỉnh sửa) cho các thành viên trong nhóm học tập."
                        ]
                    }
                }
            },
            "Chủ đề B": {
                "ten": "Mạng máy tính và Internet",
                "noi_dung": {
                    "Internet vạn vật (IoT) và Đa phương tiện": {
                        "biet": [
                            "Nêu được khái niệm Internet of Things (IoT) và một số ứng dụng tiêu biểu (nhà thông minh, nông nghiệp thông minh).",
                            "Kể tên được các thành phần cơ bản của một hệ thống IoT: cảm biến, bộ xử lý, kết nối mạng, thiết bị chấp hành."
                        ],
                        "hieu": [
                            "Giải thích được vai trò của dữ liệu thu thập từ cảm biến trong điều khiển tự động.",
                            "Trình bày được tác động của IoT đối với đời sống và sản xuất."
                        ],
                        "van_dung": [
                            "Mô tả được ý tưởng ứng dụng IoT vào một bài toán học tập hoặc đời sống thực tế quanh em."
                        ]
                    }
                }
            },
            "Chủ đề C & D": {
                "ten": "Đạo đức, pháp luật và văn hóa số - Trí tuệ nhân tạo (AI)",
                "noi_dung": {
                    "Trí tuệ nhân tạo và Ứng dụng AI có trách nhiệm": {
                        "biet": [
                            "Nêu được khái niệm ban đầu về Trí tuệ nhân tạo (AI).",
                            "Nhận biết được một số ứng dụng AI quen thuộc: nhận dạng giọng nói, khuôn mặt, dịch máy, gợi ý nội dung, xe tự hành."
                        ],
                        "hieu": [
                            "Hiểu được nguyên lý cơ bản: AI học từ lượng lớn dữ liệu để đưa ra dự đoán hoặc tạo ra nội dung mới.",
                            "Nêu được các vấn đề đạo đức khi sử dụng AI: liêm chính học thuật, tin giả (Deepfake), bảo vệ dữ liệu cá nhân."
                        ],
                        "van_dung": [
                            "Sử dụng công cụ AI một cách có trách nhiệm: xem AI là trợ thủ hỗ trợ học tập, kiểm chứng thông tin do AI sinh ra và không gian lận học thuật."
                        ]
                    }
                }
            },
            "Chủ đề E": {
                "ten": "Ứng dụng tin học - Thiết kế đa phương tiện và web",
                "noi_dung": {
                    "Biên tập video và Thiết kế trực tuyến": {
                        "biet": [
                            "Biết các phần mềm, nền tảng biên tập video và thiết kế đồ họa trực tuyến (CapCut, Canva...).",
                            "Biết các thao tác cắt ghép video, thêm phụ đề, âm thanh nền, hiệu ứng chuyển cảnh."
                        ],
                        "hieu": [
                            "Hiểu được nguyên tắc xây dựng kịch bản video ngắn (storyboard) trước khi biên tập.",
                            "Giải thích được tầm quan trọng của sự hài hòa giữa hình ảnh, chữ viết và âm thanh."
                        ],
                        "van_dung": [
                            "Xây dựng được một video clip ngắn (1-3 phút) hoặc poster số giới thiệu một sản phẩm học tập hoặc thông điệp bảo vệ môi trường."
                        ]
                    }
                }
            },
            "Chủ đề F": {
                "ten": "Giải quyết vấn đề với sự trợ giúp của máy tính - Dự án Lập trình",
                "noi_dung": {
                    "Hàm và cấu trúc dữ liệu danh sách": {
                        "biet": [
                            "Nêu được khái niệm hàm và lợi ích của việc sử dụng hàm để tái sử dụng mã nguồn.",
                            "Biết cấu trúc dữ liệu danh sách (List) trong Python: cách khai báo, truy cập phần tử qua chỉ số (index)."
                        ],
                        "hieu": [
                            "Hiểu được tham số truyền vào hàm và giá trị trả về của hàm.",
                            "Hiểu các thao tác cơ bản trên danh sách: duyệt danh sách, thêm phần tử (append), xóa phần tử."
                        ],
                        "van_dung": [
                            "Viết chương trình sử dụng hàm và danh sách để giải quyết bài toán quản lý danh sách học sinh hoặc thống kê điểm số."
                        ]
                    }
                }
            }
        }
    }
}
