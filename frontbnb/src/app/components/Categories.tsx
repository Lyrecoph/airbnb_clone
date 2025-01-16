import Image from "next/image";

const Categories = () => {
    return(
        <div className="pt-3 cursor-pointer pb-6 flex items-center space-x-12">
            <div className="pb-4 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-200 hover:opacity-100">
                <Image
                    src="/beach_category.jpg"
                    alt="Category - Beach"
                    width={20}
                    height={20}
                />
                <span className="text-xs">Beach</span>
            </div>

            <div className="pb-4 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-200 hover:opacity-100">
                <Image
                    src="/villas_category.jpg"
                    alt="Category - Villas"
                    width={20}
                    height={20}
                />
                <span className="text-xs">Villas</span>
            </div>

            <div className="pb-4 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-200 hover:opacity-100">
                <Image
                    src="/cabanes_category.jpg"
                    alt="Category - Cabins"
                    width={20}
                    height={20}
                />
                <span className="text-xs">Cabins</span>
            </div>

            <div className="pb-4 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-200 hover:opacity-100">
                <Image
                    src="/tinyHouses_category.jpg"
                    alt="Category - Tiny Houses"
                    width={20}
                    height={20}
                />
                <span className="text-xs">Tiny home</span>
            </div>
        </div>
    )
}
export default Categories;